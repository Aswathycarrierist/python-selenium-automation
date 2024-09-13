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
driver.get('https://www.target.com/')
sleep(3)
#click the sign in button
driver.find_element(By.XPATH, "//a[@data-test='@web/AccountLink']").click()
sleep(2)
#click the sign in from side navigation
driver.find_element(By.XPATH, "//a[@data-test='accountNav-signIn']").click()
sleep(2)
#verification
actual_result = driver.find_element(By.XPATH, "//h1[@class='sc-fe064f5c-0 sc-315b8ab9-2 WObnm gClYfs']").text
expected_result="Sign into your Target account"
assert expected_result in actual_result, f"Expected {expected_result} but got {actual_result}"

driver.quit()

