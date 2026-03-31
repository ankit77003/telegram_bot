import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")

# OpenRouter endpoint
url = "https://openrouter.ai/api/v1/chat/completions"

# headers
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

def get_llm_response(message):
    data = {
        "model": "gpt-3.5-turbo",  # OpenRouter supports same model names
        "messages": [{"role": "user", "content": message}]
    }

    try:
        res = requests.post(url, headers=headers, json=data)
        data = res.json()
        print("DEBUG RESPONSE:", data)

        # Handle errors
        if "error" in data:
            return f"LLM API Error: {data['error']['message']}"

        # OpenRouter response structure is same as OpenAI
        return data["choices"][0]["message"]["content"]

    except Exception as e:
        print("LLM ERROR:", e)
        return "Something went wrong with LLM"