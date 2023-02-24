import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)
driver.get("https://www.facebook.com/")
driver.find_element(By.LINK_TEXT, "Create new account").click()

driver.find_element(By.NAME,"firstname").send_keys("jhon")
driver.find_element(By.NAME,"lastname").send_keys("bodom")
driver.find_element(By.NAME,"reg_email__").send_keys("welcomw")
driver.find_element(By.ID,"password_step_input").send_keys("welcome123")
select_date = Select(driver.find_element(By.ID, "day"))
select_date.select_by_visible_text("20")
select_date = Select(driver.find_element(By.ID, "month"))
select_date.select_by_visible_text("Dec")
select_date = Select(driver.find_element(By.ID, "year"))
select_date.select_by_visible_text("1999")
driver.find_element(By.XPATH,"//input[@value='-1']").click()
time.sleep(5)
driver.find_element(By.NAME,"websubmit").click()
time.sleep(5)
