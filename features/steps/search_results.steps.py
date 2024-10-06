import time

from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

# @when('Search for {product}')
# def search_product(context, product):
#     # Search field => enter
#     context.driver.find_element(By.ID, 'search').send_keys(product)
#     # Search button => click
#     context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
#     sleep(5)  # wait for search results page to load
ADD_TO_CART_BTN = (By.CSS_SELECTOR,"[id*='addToCartButton']")
# ADD_TO_CART_BTN = (By.XPATH, '/html[1]/body[1]/div[1]/div[2]/main[1]/div[1]/div[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/button[1]')
ADD_TO_CART_BTN_SIDE_NAV = (By.CSS_SELECTOR, "[data-test='content-wrapper'] [id*='addToCart']")
SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='content-wrapper'] h4")
PRODUCT_TITLE = (By.CSS_SELECTOR, "[data-test='product-title']")
LISTINGS = (By.CSS_SELECTOR, "[data-test='@web/site-top-of-funnel/ProductCardWrapper']")
PRODUCT_IMG=(By.CSS_SELECTOR,"img")

@when('click on add to the cart button')
def click_cart_icon(context):
    sleep(15)
    # # context.driver.find_element(*ADD_TO_CART_BTN).click()
    # context.driver.wait.until(EC.visibility_of_element_located(ADD_TO_CART_BTN))
    context.driver.find_element(*ADD_TO_CART_BTN).click()
    context.driver.wait.until(EC.visibility_of_element_located(SIDE_NAV_PRODUCT_NAME))

    # add_to_cart_btn.click()


#"[data-test='chooseOptionsButton']").click()

#[id*='addToCartButtonOrTextIdFor']"

@when('confirm add to cart button from side navigation')
def side_navigation_click(context):
    context.driver.find_element(*ADD_TO_CART_BTN_SIDE_NAV).click()
    sleep(5)
#
# @then('verify correct search result shown for{product}')
# def verify_results(context,product):
#     actual_result = context.driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
#assert product in actual_result, f'Expected {product}, got actual {actual_result}'


@when('click view cart and check out')
def   click_the_view_cart_check_out(context):

      context.driver.find_element(By.CSS_SELECTOR,"[href='/cart']").click()
      sleep(5)


@then('verify cart has {amount} item')
def verify_cart_item(context, amount):
    sleep(5)
    cart_summary =context.driver.find_element(By.CSS_SELECTOR, 'div[class*="h-text-grayDark"] span').text
    assert amount in cart_summary, f"Expected {amount},items but got actual {cart_summary}"

#(By.XPATH,"//div[@data-test='resultsHeading']").text

#$$("[data-test='@web/site-top-of-funnel/ProductCardWrapper']")

@then('Verify that every product has a name and an image')
def verify_products_name_img(context):
    # To see ALL listings (comment out if you only check top ones):
    context.driver.execute_script("window.scrollBy(0,2000)", "")
    sleep(4)
    context.driver.execute_script("window.scrollBy(0,2000)", "")

    all_products = context.driver.find_elements(*LISTINGS)  # [WebEl1, WebEl2, WebEl3, WebEl4]

    for product in all_products:
        title = product.find_element(*PRODUCT_TITLE).text
        assert title, 'Product title not shown'
        print(title)
        product.find_element(*PRODUCT_IMG)