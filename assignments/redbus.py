from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)
driver.get("https://www.redbus.in/")
driver.find_element(By.ID,"i-icon-profile").click()
driver.find_element(By.ID,"signInLink").click()
driver.find_element(By.XPATH,"//div[@class='mobileInput clearfix']//input").send_keys("7898")

