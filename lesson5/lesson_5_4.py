from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


for i in range(3):
    driver1 = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()))
    driver1.get("http://uitestingplayground.com/dynamicid")
    driver1.implicitly_wait(100)  # Когда страница самостоятельно не прогружается
    button1 = driver1.find_element(By.CSS_SELECTOR, ".btn")
    button1.send_keys(Keys.RETURN)

sleep(3)


for i in range(3):
    driver2 = webdriver.Firefox(service=FirefoxService(
        GeckoDriverManager().install()))
    driver2.get("http://uitestingplayground.com/dynamicid")
    button2 = driver2.find_element(By.CSS_SELECTOR, ".btn")
    button2.send_keys(Keys.RETURN)
