from selenium import webdriver
from selenium.webdriver.common.by import By

# Launch the browser
driver = webdriver.Chrome()
# Navigate to login page
driver.get("https://www.selenium.dev/selenium/web/web-form.html")
# Get title
title = driver.title

driver.implicitly_wait(0.5)
# Find elements
text_box = driver.find_element(by=By.NAME, value="my-text")
submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")
# Enter keys
text_box.send_keys("Selenium")
submit_button.click()

message = driver.find_element(by=By.ID, value="message")
text = message.text

driver.quit()

