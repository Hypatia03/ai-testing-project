import requests

error_log = """
selenium.common.exceptions.NoSuchElementException:
Unable to locate element:
{"method":"css selector","selector":"#login-button"}
"""

prompt = f"""
You are a Selenium Automation Expert.

Analyze this Selenium error.

Error:

{error_log}

Explain:

1. Root cause
2. Possible fixes
3. Better locator suggestion

Output in clear bullet points.
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