import pytest
from datetime import datetime

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs["driver"]

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        driver.save_screenshot(
            f"screenshots/fail_{timestamp}.png"
        )