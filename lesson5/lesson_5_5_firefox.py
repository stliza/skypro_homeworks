from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

for i in range(3):
    driver = webdriver.Firefox()
    driver.get("http://uitestingplayground.com/classattr")
    sleep(2)
    button = driver.find_element(By.CSS_SELECTOR, ".btn-primary").send_keys(Keys.RETURN)

driver.quit()
