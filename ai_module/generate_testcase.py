from openai import OpenAI

client = OpenAI(
    api_key="YOUR_API_KEY"
)

prompt = """
Generate software testing test cases
for SauceDemo Login Page.

Return:
1. Test Case ID
2. Title
3. Steps
4. Expected Result
5. Priority
"""

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)

print(
    response.choices[0].message.content
)