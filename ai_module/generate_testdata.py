import requests

prompt = """
Generate CSV login test data
for SauceDemo.

Columns:

username,password,expected

Generate 10 rows.
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