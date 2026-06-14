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

    def _fill_react_input(self, element_locator, value):
        element = self.wait.until(EC.element_to_be_clickable(element_locator))
        element.click()
        self.driver.execute_script(
            """
            var el = arguments[0];
            var val = arguments[1];
            var setter = Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, 'value').set;
            setter.call(el, val);
            el.dispatchEvent(new Event('input', { bubbles: true }));
            el.dispatchEvent(new Event('change', { bubbles: true }));
        """,
            element,
            value,
        )

    def fill_information(self, first_name, last_name, zip_code):

        self._fill_react_input(self.FIRST_NAME, first_name)
        self._fill_react_input(self.LAST_NAME, last_name)
        self._fill_react_input(self.ZIP_CODE, zip_code)
        return self

    def continue_checkout(self):

        button = self.wait.until(EC.element_to_be_clickable(self.CONTINUE_BUTTON))
        self.driver.execute_script("arguments[0].click();", button)
        return self

    def finish_checkout(self):

        button = self.wait.until(EC.element_to_be_clickable(self.FINISH_BUTTON))
        self.driver.execute_script("arguments[0].click();", button)
        return self

    def get_complete_text(self):

        return self.wait.until(
            EC.visibility_of_element_located(self.COMPLETE_HEADER)
        ).text