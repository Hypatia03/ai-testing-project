from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:

    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    ZIP_CODE = (By.ID, "postal-code")

    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")

    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def fill_information(
        self,
        first_name,
        last_name,
        zip_code
    ):

        first = self.wait.until(
            EC.visibility_of_element_located(
                self.FIRST_NAME
            )
        )
        first.clear()
        first.send_keys(first_name)

        last = self.wait.until(
            EC.visibility_of_element_located(
                self.LAST_NAME
            )
        )
        last.clear()
        last.send_keys(last_name)

        zip_field = self.wait.until(
            EC.visibility_of_element_located(
                self.ZIP_CODE
            )
        )
        zip_field.clear()
        zip_field.send_keys(zip_code)

    def continue_checkout(self):

        self.wait.until(
            EC.element_to_be_clickable(
                self.CONTINUE_BUTTON
            )
        ).click()

    def finish_checkout(self):

        finish_button = self.wait.until(
            EC.element_to_be_clickable(
                self.FINISH_BUTTON
            )
        )

        finish_button.click()

    def get_complete_text(self):

        return self.wait.until(
            EC.visibility_of_element_located(
                self.COMPLETE_HEADER
            )
        ).text