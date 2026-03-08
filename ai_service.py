import os
import json
from openai import OpenAI

client = None
api_key = os.getenv("OPENAI_API_KEY")

if api_key:
    client = OpenAI(api_key=api_key)


def analyze_with_ai(description):
    """
    Uses OpenAI to return structured JSON with:
    - category
    - summary
    - next_steps
    Returns None if AI is unavailable or output is invalid.
    """

    if not client:
        return None

    prompt = f"""
You are helping classify a community safety or digital wellness report.

Given the report below, return valid JSON only with this exact shape:
{{
  "category": "string",
  "summary": "string",
  "next_steps": ["step 1", "step 2", "step 3"]
}}

Rules:
- Keep the tone calm and practical.
- The category should be concise, such as:
  "Phishing / Scam", "Phone Scam", "Network Safety", "Investment Scam", "General Advisory"
- Summary should be 1-2 sentences max.
- next_steps must contain exactly 3 items.
- No markdown.
- No extra text.

Report:
{description}
"""

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2
        )

        raw = response.choices[0].message.content.strip()
        parsed = json.loads(raw)

        if (
            "category" in parsed
            and "summary" in parsed
            and "next_steps" in parsed
            and isinstance(parsed["next_steps"], list)
            and len(parsed["next_steps"]) == 3
        ):
            return parsed

        return None

    except Exception:
        return None