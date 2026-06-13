from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Khởi tạo Chrome
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)

# Mở website demo testing
driver.get("https://www.saucedemo.com/")

# Phóng to cửa sổ
driver.maximize_window()

time.sleep(2)

# Nhập username
driver.find_element(By.ID, "user-name").send_keys("standard_user")

# Nhập password
driver.find_element(By.ID, "password").send_keys("secret_sauce")

# Click Login
driver.find_element(By.ID, "login-button").click()

time.sleep(3)

# Kiểm tra login thành công
if "inventory" in driver.current_url:
    print("TEST PASS")
else:
    print("TEST FAIL")

time.sleep(3)

driver.quit()