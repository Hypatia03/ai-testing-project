import csv
import os

import pytest

from selenium.webdriver.common.by import By

from ai_module.analyze_error import (
    analyze_error
)


def load_test_data():

    csv_path = "testdata/generated_login_data.csv"

    if not os.path.exists(csv_path):

        raise FileNotFoundError(
            f"CSV file not found: {csv_path}"
        )

    with open(
        csv_path,
        newline="",
        encoding="utf-8"
    ) as file:

        return list(
            csv.DictReader(file)
        )


test_data = load_test_data()


@pytest.mark.parametrize(
    "data",
    test_data
)
def test_login(driver, data):

    try:

        driver.maximize_window()

        driver.get(
            "https://www.saucedemo.com"
        )

        driver.find_element(
            By.ID,
            "user-name"
        ).clear()

        driver.find_element(
            By.ID,
            "user-name"
        ).send_keys(
            data["username"]
        )

        driver.find_element(
            By.ID,
            "password"
        ).clear()

        driver.find_element(
            By.ID,
            "password"
        ).send_keys(
            data["password"]
        )

        driver.find_element(
            By.ID,
            "login-button"
        ).click()

        current_url = driver.current_url

        expected = (
            data["expected"]
            .strip()
            .upper()
        )

        # PASS CASE
        if expected == "PASS":

            assert (
                "inventory.html"
                in current_url
            )

        # FAIL CASE
        else:

            assert (
                "inventory.html"
                not in current_url
            )

            error_message = driver.find_element(
                By.CSS_SELECTOR,
                "[data-test='error']"
            ).text

            assert (
                len(error_message)
                > 0
            )

            if (
                data["username"]
                == "locked_out_user"
            ):

                assert (
                    "locked out"
                    in error_message.lower()
                )

    except Exception as e:

        print(
            "\nGenerating AI Error Analysis..."
        )

        os.makedirs(
            "reports",
            exist_ok=True
        )

        ai_result = analyze_error(
            str(e)
        )

        with open(
            "reports/ai_error_analysis.md",
            "w",
            encoding="utf-8"
        ) as file:

            file.write(
                ai_result
            )

        print(
            "AI analysis saved."
        )

        raise