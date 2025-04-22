import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="class")
def init_driver(request):
    chrome_options = Options()
    chrome_options.add_argument('--ignore-certificate-errors')  # Ignora errores de certificado SSL
    chrome_options.add_argument('--allow-running-insecure-content')  # Permite contenido inseguro
    chrome_options.add_argument('start-maximized')
    web_driver = webdriver.Chrome(options=chrome_options)
    request.cls.driver = web_driver
    yield
    web_driver.quit()