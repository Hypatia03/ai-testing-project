from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def test_checkout(driver):

    # Open website
    driver.get(
        "https://www.saucedemo.com/"
    )

    # Login
    login_page = LoginPage(driver)

    login_page.login(
        "standard_user",
        "secret_sauce"
    )

    WebDriverWait(driver, 10).until(
        lambda d: "inventory" in d.current_url
    )

    print("\nAfter Login:")
    print(driver.current_url)

    # Add product
    inventory_page = InventoryPage(driver)

    inventory_page.add_backpack()

    # Open cart
    cart_page = CartPage(driver)

    cart_page.open_cart()

    WebDriverWait(driver, 10).until(
        lambda d: "cart" in d.current_url
    )

    print("\nAfter Open Cart:")
    print(driver.current_url)

    # Checkout
    cart_page.click_checkout()

    WebDriverWait(driver, 10).until(
        lambda d: "checkout-step-one" in d.current_url
    )

    print("\nAfter Click Checkout:")
    print(driver.current_url)

    # Debug page title
    print("\nPage Title:")
    print(driver.title)

    # Debug first-name field exists?
    try:
        first_name = driver.find_element(
            By.ID,
            "first-name"
        )

        print("\nFound first-name field")
        print(first_name.is_displayed())

    except Exception as e:
        print("\nCannot find first-name")
        print(e)

    # Fill checkout info
    checkout_page = CheckoutPage(driver)

    checkout_page.fill_information(
        "Nguyen",
        "Han",
        "700000"
    )

    checkout_page.continue_checkout()

    print("\nAfter Continue:")
    print(driver.current_url)

    try:
        error = driver.find_element(
            By.CSS_SELECTOR,
            "h3[data-test='error']"
        )

        print("\nValidation Error:")
        print(error.text)

    except:
        print("\nNo validation error")

    print("\nPage Source Snippet:")
    print(driver.page_source[:3000])