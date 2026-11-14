from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def obtener_texto_logotipo(self):
        logotipo = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "app_logo")))
        return logotipo.text

    def obtener_titulo(self):
        titulo = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-test='title']")))
        return titulo.text

    def obtener_productos(self):
        return self.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item")))

    def obtener_nombre_primer_producto(self):
        productos = self.obtener_productos()
        return productos[0].find_element(By.CLASS_NAME, "inventory_item_name").text

    def obtener_precio_primer_producto(self):
        productos = self.obtener_productos()
        return productos[0].find_element(By.CLASS_NAME, "inventory_item_price").text

    def menu_visible(self):
        menu = self.driver.find_element(By.ID, "react-burger-menu-btn")
        return menu.is_displayed()

    def filtro_visible(self):
        filtro = self.driver.find_element(By.CLASS_NAME, "product_sort_container")
        return filtro.is_displayed()

    def inventario_visible(self):
        inventario = self.wait.until(EC.visibility_of_element_located((By.ID, "inventory_container")))
        return inventario.is_displayed()

    def ordenar_por_precio(self):
        filtro = self.driver.find_element(By.CLASS_NAME, "product_sort_container")
        Select(filtro).select_by_visible_text("Price (low to high)")

    def obtener_precios(self):
        elementos_precios = self.driver.find_elements(By.CLASS_NAME, "inventory_item_price")
        precios = []
        for elemento_precio in elementos_precios:
            precio = float(elemento_precio.text.replace("$", ""))
            precios.append(precio)
        return precios

    def agregar_primer_producto(self):
        productos = self.obtener_productos()
        productos[0].find_element(By.TAG_NAME, "button").click()

    def ir_al_carrito(self):
        carrito = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link")))
        carrito.click()
