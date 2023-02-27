import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.medibuddy.in/")
driver.find_element(By.LINK_TEXT, "Login").click()
driver.find_element(By.XPATH, "//div[@ng-click='linkAccount()']").click()
driver.find_element(By.XPATH,"//div[@class='coperate']").click()
driver.find_element(By.NAME,"userName").send_keys("john")
driver.find_element(By.XPATH,"//button[@type='submit']").click()
driver.find_element(By.NAME,"password").send_keys("john123")
driver.find_element(By.XPATH,"//button[@type='submit']").click()

a= driver.find_element(By.XPATH,"//div[@ng-if='isPasswordWrong']").text
print(a)
time.sleep(4)