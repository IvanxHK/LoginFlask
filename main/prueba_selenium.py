from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Obtener la versión de Chrome instalada en tu sistema
chrome_version = "119.0.6045.124"

# Configurar el controlador de Chrome usando WebDriverManager con la versión específica
driver = webdriver.Chrome(ChromeDriverManager(version=chrome_version).install())

try:
    # Abrir la aplicación Flask en local
    driver.get("http://localhost:5000/login")

    # Realizar el inicio de sesión
    username_input = driver.find_element_by_name("username")
    password_input = driver.find_element_by_name("password")
    login_button = driver.find_element_by_name("login")

    username_input.send_keys("usuario")
    password_input.send_keys("contraseña")
    login_button.click()

    # Verificar que el inicio de sesión fue exitoso
    assert "¡Hola, usuario!" in driver.page_source

finally:
    # Cerrar el navegador al finalizar
    driver.quit()
