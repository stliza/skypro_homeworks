from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("https://the-internet.herokuapp.com/add_remove_elements/")

for x in range(5):
    driver.find_element(By.CSS_SELECTOR, "button").send_keys(Keys.RETURN)

print(f'Number of added elements in Firefox: '
      f'{len(driver.find_elements(By.CSS_SELECTOR, ".added-manually"))}')

driver.quit()




