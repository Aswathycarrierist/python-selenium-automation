from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import Page
from time import sleep


class HelpPage(Page):
    HEADER_RETURNS = (By.XPATH, "//h1[contains(text(), 'Return')]")

    TOPIC_SELECTION = (By.CSS_SELECTOR, "select[id*='viewHelpTopics']")

    HEADER_TARGET_CIRCLE= (By.XPATH, "//h1[contains(text(), 'About Target Circle')]");


def open_help_page_and_returns(self):
    self.open('https://help.target.com/help/SubCategoryArticle?childcat=Returns&parentcat=Returns+%26+Exchanges.')


def select_topics(self):
    dd = self.find_element(*self.TOPIC_SELECTION)
    select = Select(dd)
    select.select.by_value("Target Circle™")
    sleep(8)


def verify_help_page_opened(self):
    self.wait_for_element_to_appear(*self.HEADER_RETURNS)


def verify_Target_Circle_opened(self):
    self.wait_for_element_to_appear(*self.HEADER_TARGET_CIRCLE)
