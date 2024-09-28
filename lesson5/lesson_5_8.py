from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By


driver1 = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))
driver1.get("http://the-internet.herokuapp.com/login")
input_username1 = driver1.find_element(By.CSS_SELECTOR, "#username")
input_username1.send_keys("tomsmith")
input_password1 = driver1.find_element(By.CSS_SELECTOR, "#password")
input_password1.send_keys("SuperSecretPassword!")
button1 = driver1.find_element(By.CSS_SELECTOR, ".fa-sign-in").click()

sleep(5)

driver2 = webdriver.Firefox(service=FirefoxService(
    GeckoDriverManager().install()))
driver2.get("http://the-internet.herokuapp.com/login")
input_username2 = driver2.find_element(By.CSS_SELECTOR, "#username")
input_username2.send_keys("tomsmith")
input_password2 = driver2.find_element(By.CSS_SELECTOR, "#password")
input_password2.send_keys("SuperSecretPassword!")
button2 = driver2.find_element(By.CSS_SELECTOR, ".fa-sign-in").click()