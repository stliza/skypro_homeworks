from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("http://the-internet.herokuapp.com/login")
input_username = driver.find_element(By.CSS_SELECTOR, "#username")
input_username.send_keys("tomsmith")
input_password = driver.find_element(By.CSS_SELECTOR, "#password")
input_password.send_keys("SuperSecretPassword!")
button1 = driver.find_element(By.CSS_SELECTOR, ".fa-sign-in").click()

sleep(5)

driver.quit()
