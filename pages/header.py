from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page

class Header(Page):
    CART_BTN = (By.CSS_SELECTOR, "[data-test='@web/CartIcon']")
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_BTN =  (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
    SIGN_IN_BTN = (By.XPATH,"//a[@data-test='@web/AccountLink']")
    SIDE_NAV_SIGN_IN = (By.XPATH, "//a[@data-test='accountNav-signIn']")
    def search_product(self, product):
        self.input_text(product, *self.SEARCH_FIELD)
        # self.find_element(*self.SEARCH_FIELD).send_keys(product)
        self.click(*self.SEARCH_BTN)
        sleep(6)

    def click_cart(self):
        self.click(*self.CART_BTN)

    def click_sign_in_button(self):
        self.click(*self.SIGN_IN_BTN)

    def click_sign_in_nav_button(self):
        self.click(*self.SIDE_NAV_SIGN_IN)