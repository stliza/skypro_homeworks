from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get(
    "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
driver.implicitly_wait(20)
award = driver.find_element(By.ID, "award")
src = award.get_attribute("src")

print(src)

driver.quit()
