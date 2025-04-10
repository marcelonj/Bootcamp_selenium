from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage():
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 30)

    def wait_until_locator_present(self, locator):
        return self.wait.until(EC.presence_of_element_located((By.XPATH, locator)))
    
    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, locator))).click()