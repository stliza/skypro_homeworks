from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By


driver1 = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))
driver1.get(" http://the-internet.herokuapp.com/inputs")
search_input1 = driver1.find_element(By.CSS_SELECTOR, "input")
search_input1.send_keys("1000")

sleep(5)

search_input1.clear()
search_input1.send_keys("999")

sleep(10)

driver2 = webdriver.Firefox(service=FirefoxService(
    GeckoDriverManager().install()))
driver2.get(" http://the-internet.herokuapp.com/inputs")
search_input2 = driver2.find_element(By.CSS_SELECTOR, "input")
search_input2.send_keys("1000")

sleep(5)

search_input2.clear()
search_input2.send_keys("999")