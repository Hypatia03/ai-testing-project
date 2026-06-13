import requests

html = """
<input
    type="submit"
    id="login-button"
    class="submit-button btn_action"
    value="Login">
"""

prompt = f"""
You are Selenium Automation Expert.

Analyze HTML.

Suggest:

1. Best XPath
2. Best CSS Selector
3. Most Stable Locator

HTML:

{html}

Output only locators.
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