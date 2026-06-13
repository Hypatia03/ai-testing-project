from selenium import webdriver

GRID_URL = "http://localhost:4444/wd/hub"

def create_driver():

    options = webdriver.ChromeOptions()

    driver = webdriver.Remote(
        command_executor=GRID_URL,
        options=options
    )

    driver.maximize_window()

    return driver