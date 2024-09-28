from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver1 = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))
driver1.get("http://the-internet.herokuapp.com/entry_ad")
button1 = driver1.find_element(By.CSS_SELECTOR, ".modal-footer")
driver1.implicitly_wait(100)  # Когда страница самостоятельно не прогружается

button1.click()


driver2 = webdriver.Firefox(service=FirefoxService(
    GeckoDriverManager().install()))
driver2.get("http://the-internet.herokuapp.com/entry_ad")
button2 = driver2.find_element(By.CSS_SELECTOR, ".modal-footer")

button2.click()