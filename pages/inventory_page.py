from selenium.webdriver.common.by import By


class InventoryPage:

    ADD_BACKPACK = (
        By.ID,
        "add-to-cart-sauce-labs-backpack"
    )

    CART_BADGE = (
        By.CLASS_NAME,
        "shopping_cart_badge"
    )

    def __init__(self, driver):
        self.driver = driver

    def add_backpack(self):
        self.driver.find_element(
            *self.ADD_BACKPACK
        ).click()

    def get_cart_count(self):

        return self.driver.find_element(
            *self.CART_BADGE
        ).text