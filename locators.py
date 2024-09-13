from dataclasses import field

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get("https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&")
sleep(5)

#locate element Amazon logo
driver.find_element(By.XPATH ,"//i[@aria-label='Amazon']")
#locate email field()
driver.find_element(By.ID, 'ap_email')
#find element continue button
driver.find_element(By.ID ,'continue')
#contion of use link
sleep(3)
driver.find_element(By.XPATH, "//a[text()='Conditions of Use']")
#privacy notice link
driver.find_element(By.XPATH,"//a[@href='/gp/help/customer/display.html/ref=ap_signin_notification_privacy_notice?ie=UTF8&nodeId=468496']")

#NEED HELP find element
driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']")
#forgot password link
driver.find_elements(By.ID,'auth-fpp-link-bottom')
#other issues with sign in
driver.find_element(By.ID,'ap-other-signin-issues-link')
#create amazon account
driver.find_element(By.ID,'createAccountSubmit')