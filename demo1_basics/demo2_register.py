import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)
driver.get("https://www.facebook.com/")
driver.find_element(By.LINK_TEXT, "Create new account").click()

driver.find_element(By.NAME,"firstname").send_keys("jhon")
driver.find_element(By.NAME,"lastname").send_keys("bodom")
driver.find_element(By.NAME,"reg_email__").send_keys("welcomw")
driver.find_element(By.ID,"password_step_input").send_keys("welcomw123")
driver.find_element(By.XPATH,"//input[@value='-1']").click()
driver.find_element(By.NAME,"websubmit").click()
time.sleep(5)
