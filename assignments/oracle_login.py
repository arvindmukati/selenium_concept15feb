import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(20)
driver.get("https://www.oracle.com/in/database/")
driver.find_element(By.ID,"acctBtnLabel").click()
driver.find_element(By.LINK_TEXT,"Sign-In").click()

print(driver.title)
actual_header = driver.find_element(By.XPATH,"//h2[contains(test(),'Oracle account')]").text
print(actual_header)
driver.find_element(By.ID, "sso_username").send_keys("arvind@gmail.com")
driver.find_element(By.ID, "ssopassword").send_keys("arvind@gmail.com")
driver.find_element(By.ID, "signin_button").click()
actual_error = driver.find_element(By.XPATH,"//div[contains(text(),'Invalid username and/or password')")
print(actual_error)
time.sleep(3)
