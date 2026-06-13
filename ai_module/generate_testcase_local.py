import requests

prompt = """
You are a Senior Software Test Engineer.

Create software testing test cases for SauceDemo Login Page.

Website:
https://www.saucedemo.com

Valid Account:
username = standard_user
password = secret_sauce

IMPORTANT:

- Generate UI Testing test cases only.
- Do NOT generate API test cases.
- Do NOT generate HTTP requests.
- Do NOT generate code.
- Focus on login functionality.
- Include positive and negative scenarios.
- Output as a markdown table.

Columns:

| Test Case ID |
| Title |
| Precondition |
| Test Steps |
| Test Data |
| Expected Result |
| Priority |

Generate 10 test cases.
"""

response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "deepseek-r1:1.5b",
        "prompt": prompt,
        "stream": False
    }
)

result = response.json()

print(result["response"])