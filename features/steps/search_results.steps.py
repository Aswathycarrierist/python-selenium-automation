from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


# @when('Search for {product}')
# def search_product(context, product):
#     # Search field => enter
#     context.driver.find_element(By.ID, 'search').send_keys(product)
#     # Search button => click
#     context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
#     sleep(5)  # wait for search results page to load

@when('click on add to the cart button')
def click_cart_icon(context):
    sleep(5)
    context.driver.find_element(By.CSS_SELECTOR,"[id*='addToCartButton']").click()
    sleep(5)
#"[data-test='chooseOptionsButton']").click()

#[id*='addToCartButtonOrTextIdFor']"

@when('confirm add to cart button from side navigation')
def side_navigation_click(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='orderPickupButton']").click()
    sleep(6)

#
# @then('verify correct search result shown for{product}')
# def verify_results(context,product):
#     actual_result = context.driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
#assert product in actual_result, f'Expected {product}, got actual {actual_result}'


@when('click view cart and check out')
def   click_the_view_cart_check_out(context):
      sleep(6)
      context.driver.find_element(By.CSS_SELECTOR,"[href='/cart']").click()
      sleep(5)


@then('verify cart has {amount} item')
def verify_cart_item(context, amount):
    sleep(5)
    cart_summary =context.driver.find_element(By.CSS_SELECTOR, 'div[class*="h-text-grayDark"] span').text
    assert amount in cart_summary, f"Expected {amount},items but got actual {cart_summary}"

#(By.XPATH,"//div[@data-test='resultsHeading']").text