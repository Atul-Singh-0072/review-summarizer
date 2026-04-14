import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

def summarize_review(text):
    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",  # ✅ WORKING MODEL
            messages=[
                {"role": "system", "content": "Summarize the sentiment in 1 line"},
                {"role": "user", "content": text}
            ],
            temperature=0.5,
            max_tokens=60
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        print(f"API Error: {e}")
        return "Summary not available"