import os
from ai_module.ollama_client import ask_ai


PROMPT = """
You are a Senior Selenium Automation Engineer.

Generate Selenium Python code only.

Scenario:
Login to SauceDemo.

URL:
https://www.saucedemo.com

Username:
standard_user

Password:
secret_sauce

Requirements:
- Selenium 4
- Python
- Use By.ID
- Use WebDriverWait instead of time.sleep
- Open browser
- Login
- Verify successful login
- Close browser

IMPORTANT:
Output ONLY executable Python code.
Do not explain.
Do not use markdown.
Do not wrap with ```python
"""


def generate_script():

    result = ask_ai(PROMPT)

    # Xóa markdown nếu AI lỡ sinh ra
    result = result.replace("```python", "")
    result = result.replace("```", "")

    os.makedirs(
        "reports",
        exist_ok=True
    )

    with open(
        "reports/generated_script.py",
        "w",
        encoding="utf-8"
    ) as f:
        f.write(result)

    print(
        "Generated reports/generated_script.py"
    )


if __name__ == "__main__":
    generate_script()