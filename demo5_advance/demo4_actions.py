import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.google.com/")

action = webdriver.ActionChains(driver)

action.key_down(webdriver.Keys.SHIFT).send_keys("Hello World in ")\
    .key_up(webdriver.Keys.SHIFT).pause(1).send_keys(webdriver.Keys.ARROW_DOWN)\
    .send_keys(webdriver.Keys.ARROW_DOWN).pause(1).click().perform()

time.sleep(4)
