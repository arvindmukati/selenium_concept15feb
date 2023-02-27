import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.ilovepdf.com/excel_to_pdf")
driver.find_element(By.XPATH,"//input[@type='file']").send_keys(r"C:\Resideo\Docs\BLEDisconnect.xlsx")
time.sleep(4)