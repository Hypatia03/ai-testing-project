import os

from ai_module.ollama_client import ask_ai


def analyze_error(error_text):

    prompt = f"""
Bạn là Senior QA Automation Engineer.

Hãy phân tích lỗi Selenium sau đây.

Trả lời bằng tiếng Việt.

Format:

=== PHÂN TÍCH LỖI ===

Nguyên nhân:
...

Mức độ nghiêm trọng:
...

Cách khắc phục:
...

Locator đề xuất:
...

Code fix đề xuất:
...

Lỗi:

{error_text}
"""

    try:

        result = ask_ai(prompt)

    except Exception as e:

        result = f"""
=== PHÂN TÍCH LỖI ===

Không thể gọi AI.

Chi tiết:

{str(e)}

Lỗi gốc:

{error_text}
"""

    os.makedirs(
        "reports",
        exist_ok=True
    )

    with open(
        "reports/error_analysis.txt",
        "w",
        encoding="utf-8"
    ) as f:
        f.write(result)

    return result