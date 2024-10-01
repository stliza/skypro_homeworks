from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://the-internet.herokuapp.com/inputs")
search_input = driver.find_element(By.CSS_SELECTOR, "input")
search_input.send_keys("1000")

sleep(5)

search_input.clear()
search_input.send_keys("999")

sleep(5)

driver.quit()
