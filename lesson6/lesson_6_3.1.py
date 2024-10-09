from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get(
    "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
waiter = WebDriverWait(driver, 10)
waiter.until(
    EC.visibility_of(By.ID, "award")
    )
award = driver.find_element(By.ID, "award")
src = award.get_attribute("src")
print(src)

driver.quit()
