from .baseTest import BaseTest
from Pages.google_page import GooglePage
import pytest

class TestPrectice(BaseTest):
    def test_radio_button(self):
        practicPage = GooglePage(self.driver)
        practicPage.navToPracticeAndClickRadio2()