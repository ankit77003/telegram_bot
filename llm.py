import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")

# OpenAI API endpoint
url = "https://api.openai.com/v1/chat/completions"

# headers
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

def get_llm_response(message):
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": message}]
    }

    try:
        res = requests.post(url, headers=headers, json=data)
        data = res.json()
        print("DEBUG RESPONSE:", data)

        # If API returns an error (like quota exceeded)
        if "error" in data:
            return f"LLM API Error: {data['error']['message']}"

        # normal response
        return data["choices"][0]["message"]["content"]

    except Exception as e:
        print("LLM ERROR:", e)
        return "Something went wrong with LLM"