from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep




@given('open target main page')
def open_main(context):
    context.driver.get('https://www.target.com/')
#sleep(8)


#@when('click on the cart icon')
#def click_cart_icon(context):
   # context.driver.find_element(By.CSS_SELECTOR,"[data-test='@web/CartIcon']").click()



@when('Search for {product}')
def search_product(context, product):
    # Search field => enter
    context.driver.find_element(By.ID, 'search').send_keys(product)
    # Search button => click
    context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
  #  sleep(5)  # wait for search results page to load


@then('verify correct search result shown for {product}')
def verify_results(context, product):
    actual_result = context.driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text

    assert product in actual_result, f'Expected {product}, got actual {actual_result}'
