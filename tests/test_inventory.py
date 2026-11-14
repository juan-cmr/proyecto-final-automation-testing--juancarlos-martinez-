import logging
import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_inventory(capturar_fallo):
    driver = webdriver.Firefox()
    
    try:
        logging.info("Inicio de la prueba de inventario")
        # Iniciar sesión
        driver.get("https://www.saucedemo.com/")
        
        login = LoginPage(driver)
        logging.info("Iniciando sesión para consultar el inventario")
        login.escribir_usuario("standard_user")
        login.escribir_password("secret_sauce")
        login.presionar_login()
        inventario = InventoryPage(driver)
        
        # Comprobar el título de la página
        assert driver.title == "Swag Labs"
        
        # Comprobar los productis
        productos = inventario.obtener_productos()
        logging.info("Productos encontrados en el inventario: %s", len(productos))
              # si se quiere ver cuantos elementos hay: print(len(productos))
        assert len(productos) > 0
        
        nombre_producto = inventario.obtener_nombre_primer_producto()
        precio_producto = inventario.obtener_precio_primer_producto()
        
        assert nombre_producto == "Sauce Labs Backpack"
        assert precio_producto == "$29.99"
        
        #verificat el menu
        assert inventario.menu_visible()
        
        #verificar filtro
        assert inventario.filtro_visible()
        logging.info("Productos, nombre, precio, menú y filtro comprobados")
        
    except Exception:
        logging.exception("Falló la prueba de inventario")
        capturar_fallo(driver)
        raise
    finally:
        driver.quit()


def test_ordenamiento_por_precio(capturar_fallo):
    driver = webdriver.Firefox()

    try:
        logging.info("Inicio de la prueba de ordenamiento por precio")
        driver.implicitly_wait(10)
        driver.get("https://www.saucedemo.com/")

        login = LoginPage(driver)
        login.escribir_usuario("standard_user")
        login.escribir_password("secret_sauce")
        login.presionar_login()

        inventario = InventoryPage(driver)
        assert inventario.inventario_visible()
        logging.info("Inventario visible después de iniciar sesión")

        inventario.ordenar_por_precio()
        logging.info("Ordenamiento de menor a mayor precio seleccionado")
        precios = inventario.obtener_precios()

        assert len(precios) > 0
        assert precios == sorted(precios)
        logging.info("Precios ordenados correctamente: %s", precios)

    except Exception:
        logging.exception("Falló la prueba de ordenamiento por precio")
        capturar_fallo(driver)
        raise
    finally:
        driver.quit()
