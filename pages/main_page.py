from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep


class MainPage(Page):
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")
    O_CART_BTN_SIDE_NAV = (By.CSS_SELECTOR, "[data-test='content-wrapper'] [id*='addToCart']")

    def open_main(self):
        self.open('https://www.target.com/')


    def click_cart_icon(self):
        sleep(5)
        self.click(*self.ADD_TO_CART_BTN)


    def side_navigation_click(self):
       self.click(*self.O_CART_BTN_SIDE_NAV)
       sleep(5)