import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")

def get_llm_response(message):
    try:
        res = requests.post(url, headers=headers, json=data)
        data = res.json()

        print("DEBUG RESPONSE:", data)

        # 👇 handle error safely
        if "error" in data:
            return f"API Error: {data['error']['message']}"

        return data["choices"][0]["message"]["content"]

    except Exception as e:
        print("LLM ERROR:", e)
        return "Something went wrong with LLM"