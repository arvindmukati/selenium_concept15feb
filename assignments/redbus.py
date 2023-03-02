import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)
driver.get("https://www.redbus.in/")
driver.find_element(By.ID,"i-icon-profile").click()
driver.find_element(By.ID,"signInLink").click()

driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@class='modalIframe']"))
driver.find_element(By.XPATH,"//div[@class='mobileInput clearfix']//input").send_keys("7898")
time.sleep(2)
error_msg = driver.find_element(By.XPATH,"//span[@class='error-message-fixed error-message-full top-fix']").text
print(error_msg)
time.sleep(3)
driver.quit