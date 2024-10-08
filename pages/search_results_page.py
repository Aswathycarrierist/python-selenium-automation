from selenium.webdriver.common.by import By

from pages.base_page import Page

class SearchResultsPage(Page):
     SEARCH_RESULT_HEADER = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")

     def verify_results(self,product):
         actual_result = self.driver.find_element(*self.SEARCH_RESULT_HEADER).text
         assert product in actual_result, f'Expected {product}, got actual {actual_result}'