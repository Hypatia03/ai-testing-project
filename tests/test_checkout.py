from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_checkout(driver):

    driver.get("https://www.saucedemo.com/")

    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")

    WebDriverWait(driver, 10).until(
        lambda d: "inventory" in d.current_url
    )

    inventory_page = InventoryPage(driver)
    inventory_page.add_backpack()

    cart_page = CartPage(driver)
    cart_page.open_cart()

    WebDriverWait(driver, 10).until(
        lambda d: "cart" in d.current_url
    )

    cart_page.click_checkout()

    WebDriverWait(driver, 10).until(
        EC.url_contains("checkout-step-one")
    )

    checkout_page = CheckoutPage(driver)

    checkout_page.fill_information("Nguyen", "Han", "700000")

    checkout_page.continue_checkout()

    WebDriverWait(driver, 10).until(
        EC.url_contains("checkout-step-two")
    )

    checkout_page.finish_checkout()

    WebDriverWait(driver, 10).until(
        EC.url_contains("checkout-complete")
    )

    assert "checkout-complete" in driver.current_url