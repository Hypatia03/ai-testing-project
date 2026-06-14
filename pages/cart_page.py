from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:

    CHECKOUT_BUTTON = (By.CSS_SELECTOR, "button[name='checkout']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_cart(self):
        self.driver.get("https://www.saucedemo.com/cart.html")
        return self

    def click_checkout(self):
        button = self.wait.until(EC.presence_of_element_located(self.CHECKOUT_BUTTON))
        self.driver.execute_script("arguments[0].click();", button)
        return self
    