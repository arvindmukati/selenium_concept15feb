import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.facebook.com/")

driver.find_element(By.ID, "email").send_keys("hello@gmai.com")
driver.find_element(By.ID, "pass").send_keys("welcome123")

driver.find_element(By.NAME,"login").click()
print(driver.title)

time.sleep(5)

driver.quit()
time.sleep(5)
