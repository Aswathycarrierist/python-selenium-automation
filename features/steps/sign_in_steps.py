from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep



@given('Open Target sign in page')
def open_target_sign_in(context):
    context.app.sign_in_page.open_target_sign_in_page()

@when('Enter incorrect email and password')
def enter_incorrect_email_password(context):
    context.app.sign_in_page.enter_email()
    sleep(2)
    context.app.sign_in_page.enter_password()
    # email_field = driver.find_element(By.ID,"username")
    # email_field.send_keys(ammu@gmail.com)
    #
    # password_field = driver.find_element(By.ID,"password")
    # password_field.send_keys('ammu1ammu2ammu3')


@when('Click log in button')
def click_sign_in_button(context):
    context.app.sign_in_page.click_log_in_button()



@then("Verify that 'We can't find your account' message is shown")
def verify_cant_find_your_account(context):
    actual_message = context.driver.find_element(By.CSS_SELECTOR,"[data-test='authAlertDisplay']").text
    expected_message = 'That password is incorrect.'
    assert actual_message == expected_message, f"Expected message: '{expected_message}', but got: '{actual_message}'"

@when('Store original window')
def store_original_window(context):
     context.original_window = context.app.sign_in_page.get_current_window()
     print('original window', context.original_window)

@when('Click on Target terms and conditions link')
def click_tc_link(context):
    context.app.sign_in_page.click_tc_link()


@then('Switch to the newly opened window')
def switch_to_new_window(context):
    context.app.sign_in_page.switch_to_new_window()



@then('Verify Terms and Conditions page is opened')
def verify_terms_and_conditions_page(context):
    context.app.sign_in_page.verify_tc_opened()
    sleep(3)

@then('user can close current page')
def close_current_page(context):
    context.app.sign_in_page.close()
    sleep(3)


@then('switch back to original')
def switch_to_original_window(context):
    context.app.sign_in_page.switch_window_by_id(context.original_window)
    sleep(3)