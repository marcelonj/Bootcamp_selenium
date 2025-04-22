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

    def changeText(self, locator, text):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, locator))).clear()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, locator))).send_keys(text)

    def returnText(self, locator):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, locator))).text
    
    def scrollToElement(self, locator):
        self.wait_until_locator_present(locator)
        element = self.driver.find_element(By.XPATH, locator)
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)

    def enterToFrame(self, locator):
        self.scrollToElement(locator)
        self.wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, locator)))