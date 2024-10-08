from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


#@when('click on the cart icon')
#def click_cart_icon(context):
   # context.driver.find_element(By.CSS_SELECTOR,"[data-test='@web/CartIcon']").click()



@then('verify cart empty message shown')
def verify_cart_empty(context):
    context.app.cart_page.verify_cart_empty()
    #expected_text ='Your cart is empty'
   # actual_text = context.driver.find_element(By.CSS_SELECTOR,"[data-test='boxEmptyMsg']").text
   # assert expected_text == actual_text, f'Expected{expected_text}did not match actual{actual_text}'


#@then verify cart has correct product





