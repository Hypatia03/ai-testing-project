import os
import pytest
import allure

from datetime import datetime
from selenium import webdriver

from ai_module.analyze_error import analyze_error


@pytest.fixture(scope="function")
def driver():

    options = webdriver.ChromeOptions()

    driver = webdriver.Remote(
        command_executor="http://localhost:4444/wd/hub",
        options=options
    )

    driver.maximize_window()

    yield driver

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        try:

            driver = item.funcargs.get("driver")

            if driver is None:
                return

            os.makedirs(
                "screenshots",
                exist_ok=True
            )

            os.makedirs(
                "logs",
                exist_ok=True
            )

            os.makedirs(
                "reports",
                exist_ok=True
            )

            timestamp = datetime.now().strftime(
                "%Y%m%d_%H%M%S"
            )

            screenshot_path = (
                f"screenshots/"
                f"fail_{item.name}_{timestamp}.png"
            )

            driver.save_screenshot(
                screenshot_path
            )

            allure.attach.file(
                screenshot_path,
                name="Failure Screenshot",
                attachment_type=allure.attachment_type.PNG
            )

            print(
                f"\n[INFO] Screenshot saved: {screenshot_path}"
            )

            # ==========================
            # Save Error Log
            # ==========================

            error_text = str(
                report.longrepr
            )

            with open(
                "logs/error.log",
                "w",
                encoding="utf-8"
            ) as f:

                f.write(error_text)

            print(
                "[INFO] Error log saved."
            )

            # ==========================
            # AI Analysis
            # ==========================

            try:

                ai_result = analyze_error(
                    error_text
                )

                with open(
                    "reports/ai_error_analysis.txt",
                    "w",
                    encoding="utf-8"
                ) as f:

                    f.write(ai_result)

                print(
                    "[INFO] AI analysis generated."
                )

            except Exception as ai_error:

                print(
                    f"[WARNING] AI Analysis Failed: {ai_error}"
                )

        except Exception as e:

            print(
                f"\n[ERROR] Screenshot failed: {e}"
            )