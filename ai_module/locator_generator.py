import os

from ai_module.ollama_client import ask_ai


HTML_SAMPLE = """
<input
    type="submit"
    id="login-button"
    class="submit-button btn_action"
    value="Login">
"""


def generate_locator():

    prompt = f"""
You are Senior Selenium Automation Engineer.

Analyze HTML.

Rules:

Priority:
1. ID
2. Name
3. CSS
4. XPath

Return only:

Best XPath:
...

Best CSS:
...

Most Stable Locator:
...

HTML:

{HTML_SAMPLE}
"""

    result = ask_ai(prompt)

    os.makedirs(
        "reports",
        exist_ok=True
    )

    with open(
        "reports/generated_locator.txt",
        "w",
        encoding="utf-8"
    ) as f:
        f.write(result)

    print(
        "Generated reports/generated_locator.txt"
    )


if __name__ == "__main__":
    generate_locator()