from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://uitestingplayground.com/textinput")
driver.find_element(By.CSS_SELECTOR, "#newButtonName").send_keys("SkyPro")
driver.find_element(By.CSS_SELECTOR, "#updatingButton").send_keys(Keys.RETURN)
txt = driver.find_element(By.CSS_SELECTOR, "#updatingButton").text

print(txt)

driver.quit()
