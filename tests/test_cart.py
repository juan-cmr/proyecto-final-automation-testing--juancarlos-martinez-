import logging
import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

def test_cart(capturar_fallo):
    driver = webdriver.Firefox()
    
    try:
        logging.info("Inicio de la prueba del carrito")
        driver.implicitly_wait(10)
        
        # Iniciar sesión
        driver.get("https://www.saucedemo.com/")
        
        login = LoginPage(driver)
        logging.info("Iniciando sesión para agregar un producto al carrito")
        login.escribir_usuario("standard_user")
        login.escribir_password("secret_sauce")
        login.presionar_login()

        # Agregar el primer producto al carrito
        inventario = InventoryPage(driver)
        nombre_producto = inventario.obtener_nombre_primer_producto()
        inventario.agregar_primer_producto()
        logging.info("Producto agregado al carrito: %s", nombre_producto)

        # Entrar al carrito y verificar el producto
        inventario.ir_al_carrito()
        logging.info("Consultando el producto dentro del carrito")
        carrito = CartPage(driver)
        nombre_producto_carrito = carrito.obtener_nombre_producto()
        assert nombre_producto_carrito == nombre_producto
        logging.info("El producto del carrito coincide con el producto agregado")
        
    except Exception:
        logging.exception("Falló la prueba del carrito")
        capturar_fallo(driver)
        raise
    finally:
        driver.quit()



   
    
