from behave import given, when, then
from time import sleep



given ('open help page and returns')
def click_help_page(context):
    context.app.help_page.open_help_page_and_returns()



when('select Help topic Target Circle')
def select_help_topic(context):
    context.app.help_page.select_help_topic()



when('verify help returns page opened')
def verify_returns_opened(context):
    context.app.help_page.verify_returns_opened()



when('verify Target Circle page opened')
def verify_target_circle(context):
    context.app.help_page.verify_target_circle()