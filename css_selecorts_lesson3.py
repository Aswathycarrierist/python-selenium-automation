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

driver.get("https://www.amazon.com/ap/register?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fref%3Dnav_logo%2F%3F_encoding%3DUTF8%26ref_%3Dnav_newcust&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")
sleep(5)
# by css ,by class

#find elements by css,by class for amazon logo
driver.find_element(By.CSS_SELECTOR, "..a-icon a-icon-logo")
#find elements fore create account by css,by class
driver.find_element(By.CSS_SELECTOR,"a-spacing-small")
#by CSS,by id for enter your name
driver.find_element(By.CSS_SELECTOR,".#ap_customer_name")
#Email by CSS,BY ID
driver.find_element(By.CSS_SELECTOR,"#ap_email")
#find password by CSS,bY ID
driver.find_element(By.CSS_SELECTOR,"#ap_password")

# enter password by css,class
driver.find_element(By.CSS_SELECTOR,".a-alert-content")

#re enter password by css,by id
driver.find_element(By.CSS_SELECTOR,"#ap_password_check")
#contion of use using css,and partial match
driver.find_element(By.CSS_SELECTOR,"[href*='notification_condition_of_use']")
#condition of use by css and attributes
driver.find_elements(By.CSS_SELECTOR, "a[href='/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088']")
#privactnotice by css with partialmatch
driver.find_element(By.CSS_SELECTOR,  "#legalTextRow  [href*='privacy_notice']")
#sign in with css and class
driver.find_element(By.CSS_SELECTOR,".a-link-emphasis")

