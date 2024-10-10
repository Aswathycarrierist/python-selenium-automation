from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page

class SignInPage(Page):
    SIGN_IN_PAGE = (By.XPATH,"//h1/span[text()='Sign into your Target account']")

    def verify_signin_opened(self):
        expected_text = 'Sign into your Target account'
        actual_text = self.driver.find_element(*self.SIGN_IN_PAGE).text
        assert expected_text == actual_text, f'Expected {expected_text} did not match actual {actual_text}'