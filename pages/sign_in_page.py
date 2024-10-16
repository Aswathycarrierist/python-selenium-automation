from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page

class SignInPage(Page):
    SIGN_IN_PAGE = (By.XPATH,"//h1/span[text()='Sign into your Target account']")
    TC_LINK = (By.CSS_SELECTOR, "[aria-label='terms & conditions - opens in a new window']")

    def verify_signin_opened(self):
        expected_text = 'Sign into your Target account'
        actual_text = self.driver.find_element(*self.SIGN_IN_PAGE).text
        assert expected_text == actual_text, f'Expected {expected_text} did not match actual {actual_text}'


    def open_target_sign_in_page(self):
        self.open('https://www.target.com/login')


    def click_tc_link(self):
        self.wait_to_be_clickable_click(*self.TC_LINK)


    def verify_tc_opened(self):
        self.verify_partial_url('/terms-conditions/')