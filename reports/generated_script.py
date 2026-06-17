
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

# Open URL
driver.get("https://www.saucedemo.com")

# Wait for username input field to load and enter username
username_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "user-name"))
)
username_input.send_keys("standard_user")

# Wait for password input field to load and enter password
password_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "password"))
)
password_input.send_keys("secret_sauce")

# Wait for login button to load and click it
login_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "login-button"))
)
login_button.click()

# Wait for page to fully load after successful login
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "title"))
)

# Verify successful login by checking if the title contains 'Products'
assert "Products" in driver.title

driver.quit()
