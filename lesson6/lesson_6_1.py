from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(20)
driver.get("http://www.uitestingplayground.com/ajax")
driver.find_element(By.CSS_SELECTOR, "#ajaxButton").click()
txt = driver.find_element(By.CSS_SELECTOR, ".bg-success").text

print(txt)

driver.quit()
