from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver1 = webdriver.Firefox(
    service=FirefoxService(GeckoDriverManager().install()))

driver1.get("https://the-internet.herokuapp.com/add_remove_elements/")
button = driver1.find_element(By.CSS_SELECTOR, "button")


for x in range(5):
    button.send_keys(Keys.RETURN)

delete1 = driver1.find_elements(By.CSS_SELECTOR, ".added-manually")

len1 = len(delete1)
print(len1)


driver2 = webdriver.Chrome(
         service=ChromeService(ChromeDriverManager().install()))
driver2.get("https://the-internet.herokuapp.com/add_remove_elements/")
button = driver2.find_element(By.CSS_SELECTOR, "button")
for x in range(5):
    button.send_keys(Keys.RETURN)
delete2 = driver2.find_elements(By.CSS_SELECTOR, ".added-manually")
len2 = len(delete2)
print(len2)

sleep(3)
