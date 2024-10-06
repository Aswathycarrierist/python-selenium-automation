from behave.formatter.ansi_escapes import colors
from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('open target product {product_id}')
def open_target(context,product_id):
    context.driver.get(f'https://www.target.com/p/{product_id}')
    sleep(8)


@then('verify user can click through colors')
def click_and_verify(context):
    expected_colors=['grey', 'dark khaki', 'navy/tan', 'stone/grey', 'white/gum', 'white/navy/red', 'white/sand/tan', 'black/gum - Out of Stock']
    actual_colors=[]
    colors = context.driver.find_elements(By.CSS_SELECTOR,"[data-test='@web/VariationComponent']:nth-child(3) ul li")
    #[webelement1,webelement2,webelement3,webelement4,webelement5]
    SELECTED_COLOR = (By.CSS_SELECTOR, "[data-test='@web/VariationComponent']:nth-child(3) div[class*='kda-dqB']")
    for color in colors:
        color.click()

        selected_color = context.driver.find_element(*SELECTED_COLOR).text
        print('Current color text', selected_color)

        selected_color = selected_color.split('\n')[1]  #
        actual_colors.append(selected_color)
        print('actual_colors list: ', actual_colors)

    assert expected_colors == actual_colors, f'Expected {expected_colors} did not match actual {actual_colors}'