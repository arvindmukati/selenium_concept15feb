import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("http://demo.openemr.io/b/openemr/")
driver.find_element(By.ID,"authUser").send_keys("admin")
driver.find_element(By.ID,"clearPass").send_keys("pass")
select_language= Select(driver.find_element(By.XPATH,"//select[@name='languageChoice']"))
select_language.select_by_value("18")
time.sleep(3)
driver.find_element(By.ID,"login-button").click()
time.sleep(3)

driver.find_element(By.XPATH,"//div[@class='menuSection dropdown']").click()
driver.find_element(By.XPATH," //div[contains(text(),'New/Search')]").click()
driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@name='pat']"))
driver.find_element(By.ID,"form_fname").send_keys("john")
driver.find_element(By.ID,"form_lname").send_keys("wick")
select_language= Select(driver.find_element(By.XPATH,"//select[@id='form_sex']"))
select_language.select_by_value("Male")
driver.find_element(By.XPATH,"//input[@id='form_DOB']").send_keys("2023-03-02")
driver.find_element(By.ID,"create").click()
driver.switch_to.default_content()
driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@id='modalframe']"))
driver.find_element(By.XPATH,"//input[@value='Confirm Create New Patient']").click()
wait = WebDriverWait(driver,100)
wait.until(expected_conditions.alert_is_present())

actual_alert = driver.switch_to.alert.text
print(actual_alert)
driver.switch_to.alert.accept()

if len(driver.find_elements(By.XPATH,"//div[@class='closeDlgIframe']"))>0:
    driver.find_element(By.XPATH,"//div[@class='closeDlgIframe']").click()

driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@name='pat']"))

actual_added_patient=driver.find_element(By.XPATH,"//i[@class='fa fa-question-circle']/ancestor::h2").text
print(actual_added_patient)
time.sleep(10)
