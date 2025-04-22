import time
from Config.locators_iframe_page import IframeLocators
from .base_page import BasePage

class IframePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def enterPage(self):
        self.driver.get("https://rahulshettyacademy.com/AutomationPractice/")

    def interactHomeLogo(self):
        try:
            self.scrollToElement(IframeLocators.iframe)
            self.click(IframeLocators.logo_home)
        except:
            print('No se puede acceder al elemento')
        time.sleep(5)

    def enterToIframeAndInteract(self):
        self.enterToFrame(IframeLocators.iframe)
        time.sleep(3)
        self.interactHomeLogo()