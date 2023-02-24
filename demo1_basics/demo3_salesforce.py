import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)
driver.get("https://www.salesforce.com/in/form/signup/freetrial-sales/")

driver.find_element(By.NAME,"UserFirstName").send_keys("jhon")
driver.find_element(By.NAME,"UserLastName").send_keys("Wick")
driver.find_element(By.NAME,"UserEmail").send_keys("jhon@gmail.com")
Select(driver.find_element(By.NAME, 'UserTitle')).select_by_value('IT_Manager_AP')
driver.find_element(By.NAME,"CompanyName").send_keys("Einfo")
Select(driver.find_element(By.NAME, 'CompanyEmployees')).select_by_value('250')
driver.find_element(By.NAME,"UserPhone").send_keys("1234")
driver.find_element(By.XPATH, "//div[@class='checkbox-ui']").click()
time.sleep(3)
driver.find_element(By.NAME, "start my free trial").click()

time.sleep(5)