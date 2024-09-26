
from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('open target circle page')
def open_main(context):
    context.driver.get('https://www.target.com/circle')
    sleep(5)


@then('verify benefit cell has 10 links')
def verify_benefit_cell_links(context):
    links =context.driver.find_elements(By.CSS_SELECTOR,"[data-test='@web/slingshot-components/CellsComponent/Link']")
    print(links)
    assert len(links) == 10,f'Expected 10 links but got {len(links)}'