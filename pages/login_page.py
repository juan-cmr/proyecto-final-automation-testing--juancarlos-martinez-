from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def escribir_usuario(self, usuario):
        campo_usuario = self.wait.until(EC.presence_of_element_located((By.ID, "user-name")))
        campo_usuario.send_keys(usuario)

    def escribir_password(self, password):
        campo_password = self.wait.until(EC.presence_of_element_located((By.ID, "password")))
        campo_password.send_keys(password)

    def presionar_login(self):
        boton_login = self.wait.until(EC.element_to_be_clickable((By.ID, "login-button")))
        boton_login.click()

    def obtener_mensaje_error(self):
        return self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='error']")))
