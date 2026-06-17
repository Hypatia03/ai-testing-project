import os

from ai_module.ollama_client import ask_ai

PROMPT = """
You are a Senior QA Engineer.

Generate test cases ONLY for SauceDemo Login.

Website:
https://www.saucedemo.com

Page contains:

- Username textbox
- Password textbox
- Login button

Valid account:

Username: standard_user
Password: secret_sauce

Generate exactly 10 UI test cases.

Include:

1. Valid login
2. Invalid username
3. Invalid password
4. Empty username
5. Empty password
6. Empty username and password
7. Locked user
8. Problem user
9. Performance glitch user
10. Logout after login

Output ONLY markdown table.

Columns:

| Test Case ID |
| Title |
| Steps |
| Expected Result |
| Priority |

No explanation.
"""

def generate_testcases():

    result = ask_ai(PROMPT)

    os.makedirs("reports", exist_ok=True)

    with open(
        "reports/generated_testcases.md",
        "w",
        encoding="utf-8"
    ) as f:
        f.write(result)

    print(
        "Generated reports/generated_testcases.md"
    )


if __name__ == "__main__":
    generate_testcases()