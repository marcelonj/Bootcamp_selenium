import time
from Config.locators_practice import PracticeLocators
from .base_page import BasePage

class GooglePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def navToPracticeAndClickRadio2(self):
        self.driver.get("https://rahulshettyacademy.com/AutomationPractice/")
        self.wait_until_locator_present(PracticeLocators.radio2)
        self.click(PracticeLocators.radio2)
        time.sleep(5)