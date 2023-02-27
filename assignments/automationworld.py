import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.automationworld.com/")
driver.find_element(By.LINK_TEXT,"Subscribe").click()
time.sleep(5)
driver.switch_to.window(driver.window_handles[1])
driver.find_element(By.ID,"id24_344").click()
driver.find_element(By.ID,"id1").send_keys("jhon")
driver.find_element(By.ID,"id2").send_keys("Wick")
driver.find_element(By.ID,"id10").send_keys("Engineer")
driver.find_element(By.ID,"id195").send_keys("www.google.com")
driver.find_element(By.ID,"id3").send_keys("Google")
driver.find_element(By.ID,"id11").send_keys("12345678990")


select_country= Select(driver.find_element(By.ID,"id7"))
select_country.select_by_value("189")
driver.find_element(By.ID,"id6").send_keys("Chennai")
driver.find_element(By.ID,"id339_2327").click()
driver.find_element(By.ID,"submitbtn").click()
error_message = driver.find_element(By.XPATH, "//li").text
print(error_message)
time.sleep(10)