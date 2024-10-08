from selenium.webdriver.common.by import By

from pages.base_page import Page

class SearchResultsPage(Page):
     SEARCH_RESULT_HEADER = (By.XPATH,"//span[contains(text(), 'for')]")


     def verify_results(self,product):
         self.verify_partial_text(product,*self.SEARCH_RESULT_HEADER)
         #actual_result = self.driver.find_element(*self.SEARCH_RESULT_HEADER).text
        # assert product in actual_result, f'Expected {product}, got actual {actual_result}'


     def verify_search_results_url(self,product):
         self.verify_partial_url(product)