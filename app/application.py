from pages.base_page import Page
from pages.cart_page import CartPage
from pages.header import Header
from pages.main_page import MainPage
from pages.search_results_page import SearchResultsPage
from pages.sign_in_page import SignInPage
from pages.help_page import HelpPage
class Application:
    def __init__(self, driver):
        self.page = Page(driver)
        self.cart_page = CartPage(driver)
        self.main_page = MainPage(driver)
        self.header = Header(driver)
        self.search_results_page = SearchResultsPage(driver)
        self.sign_in_page = SignInPage(driver)
        self.help_page = HelpPage(driver)