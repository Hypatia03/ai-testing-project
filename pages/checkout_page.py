from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:

    FIRST_NAME = (By.CSS_SELECTOR, "input[name='firstName']")
    LAST_NAME = (By.CSS_SELECTOR, "input[name='lastName']")
    ZIP_CODE = (By.CSS_SELECTOR, "input[name='postalCode']")

    CONTINUE_BUTTON = (By.CSS_SELECTOR, "input[name='continue']")
    FINISH_BUTTON = (By.CSS_SELECTOR, "button[name='finish']")
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def fill_information(self, first_name, last_name, zip_code):

        first_box = self.wait.until(EC.presence_of_element_located(self.FIRST_NAME))
        self.driver.execute_script("arguments[0].value = arguments[1];", first_box, first_name)
        self.driver.execute_script("arguments[0].dispatchEvent(new Event('input', { bubbles: true }));", first_box)

        last_box = self.wait.until(EC.presence_of_element_located(self.LAST_NAME))
        self.driver.execute_script("arguments[0].value = arguments[1];", last_box, last_name)
        self.driver.execute_script("arguments[0].dispatchEvent(new Event('input', { bubbles: true }));", last_box)

        zip_box = self.wait.until(EC.presence_of_element_located(self.ZIP_CODE))
        self.driver.execute_script("arguments[0].value = arguments[1];", zip_box, zip_code)
        self.driver.execute_script("arguments[0].dispatchEvent(new Event('input', { bubbles: true }));", zip_box)

        return self

    def continue_checkout(self):

        button = self.wait.until(EC.presence_of_element_located(self.CONTINUE_BUTTON))
        self.driver.execute_script("arguments[0].click();", button)
        return self

    def finish_checkout(self):

        button = self.wait.until(EC.presence_of_element_located(self.FINISH_BUTTON))
        self.driver.execute_script("arguments[0].click();", button)
        return self

    def get_complete_text(self):

        return self.wait.until(
            EC.visibility_of_element_located(self.COMPLETE_HEADER)
        ).text
        