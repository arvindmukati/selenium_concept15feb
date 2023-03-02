import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.royalcaribbean.com/")
driver.find_element(By.XPATH,"//div[@class='notification-banner__close']").click()
driver.find_element(By.ID,"rciHeaderSignIn").click()
driver.find_element(By.LINK_TEXT,"Create an account").click()
driver.find_element(By.XPATH,"//input[@data-placeholder='First name/Given name']").send_keys("Dennis")
driver.find_element(By.XPATH,"//input[@data-placeholder='Last name/Surname']").send_keys("Rich")
driver.find_element(By.XPATH, "//span[contains(text(),'Month')]").click()
driver.find_element(By.XPATH, "//span[contains(text(),'April')]").click()
driver.find_element(By.XPATH, "//span[contains(text(),'Day')]").click()
driver.find_element(By.XPATH, "//span[contains(text(),'4')]").click()
driver.find_element(By.XPATH, "//input[@data-placeholder='Year']").send_keys(1990)
driver.find_element(By.XPATH, "//span[contains(text(),'Country/Region of residence')]").click()
driver.find_element(By.XPATH, "(//span[contains(text(),'India')]) [2]").click()
driver.find_element(By.XPATH,"//input[@data-placeholder='Email address']").send_keys("demo@gmial.com")
driver.find_element(By.XPATH,"//input[@data-placeholder='Create new password']").send_keys("1234")
driver.find_element(By.XPATH, "//span[contains(text(),'Select one security question')]").click()
driver.find_element(By.XPATH,"//span[normalize-space()='What was your first car's make or model?']").click()
driver.find_element(By.XPATH, "//input[@data-placeholder='Answer']").send_keys("Bolero")
driver.find_element(By.XPATH,"(//span[@class='mat-checkbox-inner-container mat-checkbox-inner-container-no-side-margin'])[2]").click()
driver.find_element(By.XPATH, "//button[normalize-space()='Done']").click()

driver.quit()