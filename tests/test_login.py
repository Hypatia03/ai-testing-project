import pandas as pd
import pytest

from pages.login_page import LoginPage


data = pd.read_csv(
    "testdata/login_data.csv"
)

test_data = data.values.tolist()


@pytest.mark.parametrize(
    "username,password,expected",
    test_data
)
def test_login(
    driver,
    username,
    password,
    expected
):

    driver.get(
        "https://www.saucedemo.com/"
    )

    login_page = LoginPage(driver)

    username = "" if pd.isna(username) else str(username)
    password = "" if pd.isna(password) else str(password)

    login_page.login(
        username,
        password
    )
    
    print(
    f"Username={username}, "
    f"Password={password}, "
    f"Expected={expected}"
    )

    if expected == "pass":

        assert (
            "inventory"
            in driver.current_url
        )

    else:

        assert (
            login_page.has_error()
        )