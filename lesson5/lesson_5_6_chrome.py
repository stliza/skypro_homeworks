from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://the-internet.herokuapp.com/entry_ad")
button = driver.find_element(By.CSS_SELECTOR, ".modal-footer").click()

driver.quit()
