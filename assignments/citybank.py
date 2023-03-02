import dataclasses
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.online.citibank.co.in/")
driver.find_element(By.XPATH,"//a[@title='Close']").click()
driver.find_element(By.XPATH,"//a[@title='Login']").click()
driver.switch_to.window(driver.window_handles[1])
driver.find_element(By.XPATH,"//div[@onclick='ForgotUserID();']").click()
driver.find_element(By.XPATH,"//a[@class='sbSelector']").click()
driver.find_element(By.LINK_TEXT,"Credit Card").click()
driver.find_element(By.ID,"citiCard1").send_keys("4545")
driver.find_element(By.ID,"citiCard2").send_keys("5656")
driver.find_element(By.ID,"citiCard3").send_keys("8887")
driver.find_element(By.ID,"citiCard4").send_keys("9998")
driver.find_element(By.ID,"cvvnumber").send_keys("123")
driver.find_element(By.ID,"bill-date-long").click()
select_year= Select(driver.find_element(By.XPATH,"//select[@class='ui-datepicker-year']"))
select_year.select_by_value("2022")
select_month= Select(driver.find_element(By.XPATH,"//select[@class='ui-datepicker-month']"))
select_month.select_by_value("3")
driver.find_element(By.LINK_TEXT,"14").click()

# Approach 2
# driver.execute_script("document.querySelector('#bill-date-long').value='11/09/2001'")

# ele1 =driver.find_element(By.XPATH,"//input[@name='DOB']")
# driver.execute_script("arguments[0].value='11/09/2000'",ele1)

driver.find_element(By.XPATH,"//input[@type='button']").click()

time.sleep(3)
error_message = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/li").text
print(error_message)
time.sleep(6)