from .baseTest import BaseTest
from Pages.text_input_page import TextInputPage
import pytest

class TestPrectice(BaseTest):
    def test_change_text(self):
        textInputPage = TextInputPage(self.driver)
        textInputPage.changeTextInput()
        textInputPage.updateText()