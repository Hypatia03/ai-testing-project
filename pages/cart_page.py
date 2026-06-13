from selenium.webdriver.common.by import By


class CartPage:

    CART_LINK = (
        By.CLASS_NAME,
        "shopping_cart_link"
    )

    CHECKOUT_BUTTON = (
        By.ID,
        "checkout"
    )

    def __init__(self, driver):
        self.driver = driver

    def open_cart(self):

        self.driver.find_element(
            *self.CART_LINK
        ).click()

    def click_checkout(self):

        self.driver.find_element(
            *self.CHECKOUT_BUTTON
        ).click()