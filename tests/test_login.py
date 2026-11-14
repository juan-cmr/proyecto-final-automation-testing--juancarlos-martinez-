import logging
import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.reader import read_users_csv

@pytest.mark.parametrize("datos", read_users_csv())
def test_login(datos, capturar_fallo):
    driver = webdriver.Firefox()
    
    try:
        logging.info("Inicio del caso de login. Acceso válido esperado: %s", datos["tipo_usuario"])
        assert datos["tipo_usuario"] in ("True", "False"), "tipo_usuario debe ser 'True' o 'False' en el CSV"
        driver.implicitly_wait(10)
        driver.get("https://www.saucedemo.com/")
        
        login = LoginPage(driver)
        logging.info("Intentando iniciar sesión")
        login.escribir_usuario(datos["usuario"])
        login.escribir_password(datos["password"])
        login.presionar_login()
        
        if datos["tipo_usuario"] == "True":
            assert "/inventory.html" in driver.current_url

            # Comprobar el logotipo y el título
            inventario = InventoryPage(driver)
            assert inventario.obtener_texto_logotipo() == "Swag Labs"

            assert inventario.obtener_titulo() == "Products"
            logging.info("Login correcto. Inventario, logotipo y título comprobados")

        elif datos["tipo_usuario"] == "False":
            # Verificar el mensake de error
            mensaje_error = login.obtener_mensaje_error()
            assert mensaje_error.is_displayed()
            assert "Username and password do not match any user in this service" in mensaje_error.text
            logging.info("Mensaje de credenciales incorrectas comprobado")

    except Exception:
        logging.exception("Falló la prueba de login")
        capturar_fallo(driver)
        raise
    finally:
        driver.quit()
