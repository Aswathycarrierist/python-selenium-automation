from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page

class SignInPage(Page):
    SIGN_IN_PAGE = (By.XPATH,"//h1/span[text()='Sign into your Target account']")
    TC_LINK = (By.CSS_SELECTOR, "[aria-label='terms & conditions - opens in a new window']")
    EMAIL = 'ammu@gmail.com'
    PASSWORD = 'ammu1ammu2ammu3'
    EMAIL_FIELD = (By.ID,"username")
    PASSWORD_FIELD = (By.ID,"password")
    SIGN_IN_PASSWORD_BTN = (By.ID,"login")
    LOGIN_BTN = (By.ID,"login")


    def verify_signin_opened(self):
        expected_text = 'Sign into your Target account'
        actual_text = self.driver.find_element(*self.SIGN_IN_PAGE).text
        assert expected_text == actual_text, f'Expected {expected_text} did not match actual {actual_text}'


    def open_target_sign_in_page(self):
        self.open('https://www.target.com/login?client_id=ecom-web-1.0.0&ui_namespace=ui-default&back_button_action=browser&keep_me_signed_in=true&kmsi_default=false&actions=create_session_signin&username=ano%2A%2A%2A')

    def enter_email(self):
        self.find_element(*self.EMAIL_FIELD).send_keys(self.EMAIL)


    def enter_password(self):
        self.find_element(*self.PASSWORD_FIELD).send_keys(self.PASSWORD)

    def click_log_in_button(self):
        self.wait_to_be_clickable_click(*self.LOGIN_BTN)


    def click_tc_link(self):
        self.wait_to_be_clickable_click(*self.TC_LINK)


    def verify_tc_opened(self):
        self.verify_partial_url('/terms-conditions/')