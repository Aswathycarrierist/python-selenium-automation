from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page

class CartPage(Page):
    CART_EMPTY_TXT=(By.CSS_SELECTOR, "[data-test='boxEmptyMsg']")
    VIEW_CART_CHECK_OUT=(By.CSS_SELECTOR, "[href='/cart']")

    def verify_cart_empty(self):
        expected_text = 'Your cart is empty'
        actual_text = self.driver.find_element(*self.CART_EMPTY_TXT).text
        assert expected_text == actual_text, f'Expected {expected_text} did not match actual {actual_text}'

    def click_the_view_cart_check_out(self):
        self.click(*self.VIEW_CART_CHECK_OUT)
        sleep(5)
