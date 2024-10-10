from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when('click on the cart icon')
def click_cart_icon(context):
    context.app.header.click_cart()
   # context.driver.find_element(By.CSS_SELECTOR,"[data-test='@web/CartIcon']").click()


# @then('verify cart empty message shown')
# def verify_cart_empty(context):
#     expected_text ='Your cart is empty'
#     actual_text = context.driver.find_element(By.CSS_SELECTOR,"[data-test='boxEmptyMsg']").text
#     assert expected_text == actual_text, f'Expected{expected_text}did not match actual{actual_text}'


#Scenario2
@when('click on the sign in button')
def  click_on_the_sign_in(context):
    context.app.header.click_sign_in_button()
    #context.driver.find_element(By.XPATH,"//a[@data-test='@web/AccountLink']").click()
    sleep(2)


@when('click sigh in from side navigation menu')
def click_sign_in(context):
    context.app.header.click_sign_in_nav_button()
    #context.driver.find_element(By.XPATH, "//a[@data-test='accountNav-signIn']").click()
    sleep(3)


@then('verify sign in page opened')
def verify_signin_opened(context):
    expected_text = 'Sign into your Target account'
    actual_text = context.driver.find_element(By.XPATH,"//h1/span[text()='Sign into your Target account']").text

    assert expected_text == actual_text, f'Expected {expected_text} did not match actual {actual_text}'