from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

for i in range(3):
    driver = webdriver.Chrome()
    driver.get("http://uitestingplayground.com/dynamicid")
    button = driver.find_element(By.CSS_SELECTOR, ".btn").send_keys(Keys.RETURN)

driver.quit()