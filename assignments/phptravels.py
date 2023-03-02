import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)
driver.get("https://www.phptravels.net/home")
driver.find_element(By.XPATH,"//a[@title='flights']").click()
driver.find_element(By.NAME,"from").send_keys("Los Angles")
time .sleep(3)
action=webdriver.ActionChains(driver)
action.key_down(webdriver.Keys.ARROW_DOWN).pause(1).click().perform()
driver.find_element(By.NAME,"to").send_keys("Dallas")
action.key_down(webdriver.Keys.ARROW_DOWN).pause(1).click().perform()
time.sleep(3)
driver.find_element(By.ID,"departure").clear()
driver.find_element(By.ID,"departure").send_keys("22-05-2022")
time.sleep(3)
driver.find_element(By.XPATH,"//p[contains(text(),'Travellers ')]").click()
driver.find_element(By.XPATH,"//i[@class='la la-plus']").click()
time.sleep(3)
driver.find_element(By.ID,"flights-search").click()

driver.close()
