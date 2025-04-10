import time
from Config.locators_text_input import TextInputLocators
from .base_page import BasePage

class TextInputPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def changeTextInput(self):
        self.driver.get("http://www.uitestingplayground.com/textinput")
        self.wait_until_locator_present(TextInputLocators.input_text)
        self.changeText(TextInputLocators.input_text, "Click NOW!")
        time.sleep(5)

    def updateText(self):
        self.wait_until_locator_present(TextInputLocators.button_submit)
        self.click(TextInputLocators.button_submit)
        time.sleep(5)

    def changeAndUpdateText(self):
        self.changeTextInput()
        self.updateText()