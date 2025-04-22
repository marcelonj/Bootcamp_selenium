from .baseTest import BaseTest
from Pages.sample_app_page import SampleAppPage
from Pages.iframe_page import IframePage
import pytest

# Tests final exercise 1
class TestAppPage(BaseTest):
    def test_login_success(self):
        sampleAppPage = SampleAppPage(self.driver)
        sampleAppPage.enterSampleApp()
        sampleAppPage.login('user', 'pwd')
        assert sampleAppPage.returnStatus() == 'Welcome, user!', 'Se esperaba status "Welcome, user!"'

    def test_login_invalid_user(self):
        sampleAppPage = SampleAppPage(self.driver)
        sampleAppPage.enterSampleApp()
        sampleAppPage.login('', 'pwd')
        assert sampleAppPage.returnStatus() == 'Invalid username/password', 'Se esperaba status "Invalid username/password"'

    def test_login_invalid_password(self):
        sampleAppPage = SampleAppPage(self.driver)
        sampleAppPage.enterSampleApp()
        sampleAppPage.login('user', 'password')
        assert sampleAppPage.returnStatus() == 'Invalid username/password', 'Se esperaba status "Invalid username/password"'

# Tests final exercise 1
class TestIframe(BaseTest):
    def test_interact_without_iframe(self):
        iframePage = IframePage(self.driver)
        iframePage.enterPage()
        iframePage.interactHomeLogo()

    def test_interact_within_iframe(self):
        iframePage = IframePage(self.driver)
        iframePage.enterPage()
        iframePage.enterToIframeAndInteract()