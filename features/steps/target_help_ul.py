from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('open target help circle page')
def verify_correct_link_for_benefit_cell(context):
    context.driver.find_elements(By.CSS_SELECTOR,"action='/help/TargetGuestHelpHomeResponsive']")