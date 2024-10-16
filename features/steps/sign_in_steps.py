from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep



@given('Open Target sign in page')
def open_target_sign_in(context):
    context.app.sign_in_page.open_target_sign_in_page()


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