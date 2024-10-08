from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page

class Header(Page):
    CART_BTN = (By.CSS_SELECTOR, "[data-test='@web/CartIcon']")
    SEARCH_FIELD= (By.ID, 'search')
    SEARCH_BTN =  (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")


    def search_product(self, product):
        self.input_text(product, *self.SEARCH_FIELD)
        # self.find_element(*self.SEARCH_FIELD).send_keys(product)
        self.click(*self.SEARCH_BTN)
        sleep(6)

    def click_cart(self):
        self.click(*self.CART_BTN)
