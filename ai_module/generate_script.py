import requests

prompt = """
You are a Senior Selenium Automation Engineer.

Generate Selenium Python code for SauceDemo login.

Website:
https://www.saucedemo.com

Username:
standard_user

Password:
secret_sauce

Rules:

- Use Selenium 4 syntax.
- Use By.ID locator.
- Import By from selenium.webdriver.common.by.
- Do not use deprecated methods.
- Output only executable Python code.
- Do not explain.
"""

response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "deepseek-r1:1.5b",
        "prompt": prompt,
        "stream": False
    }
)

print(response.json()["response"])
