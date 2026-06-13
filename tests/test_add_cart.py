from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def test_add_to_cart(driver):

    driver.get(
        "https://www.saucedemo.com/"
    )

    login_page = LoginPage(driver)

    login_page.login(
        "standard_user",
        "secret_sauce"
    )

    inventory_page = InventoryPage(driver)

    inventory_page.add_backpack()

    assert (
        inventory_page.get_cart_count()
        == "1"
    )