import time
from Config.locators_sample_app import SampleAppLocators
from .base_page import BasePage

class SampleAppPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def enterSampleApp(self):
        self.driver.get("http://www.uitestingplayground.com/")
        self.wait_until_locator_present(SampleAppLocators.sample_app_link)
        self.click(SampleAppLocators.sample_app_link)

    def checkStatus(self):
        self.wait_until_locator_present(SampleAppLocators.login_status)
        return self.returnText(SampleAppLocators.login_status)
    
    def logout(self):
        if "User logged out." not in self.returnText(SampleAppLocators.login_status):
            self.click(SampleAppLocators.btn_log)

    def login(self, user, password):
        self.logout()
        self.changeText(SampleAppLocators.input_user, user)
        self.changeText(SampleAppLocators.input_password, password)
        self.click(SampleAppLocators.btn_log)
        time.sleep(5)

    def returnStatus(self):
        return self.returnText(SampleAppLocators.login_status)