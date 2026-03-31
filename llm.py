import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")

# Define URL for OpenAI chat API
url = "https://api.openai.com/v1/chat/completions"

# Define headers once
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

def get_llm_response(message):
    # Define payload for the API request
    data = {
        "model": "gpt-3.5-turbo",        # or "gpt-4o-mini" if you have access
        "messages": [{"role": "user", "content": message}]
    }

    try:
        res = requests.post(url, headers=headers, json=data)
        data = res.json()

        # Debug output to see what API returns
        print("DEBUG RESPONSE:", data)

        # Handle API errors gracefully
        if "error" in data:
            return f"LLM API Error: {data['error']['message']}"

        # Return the assistant reply
        return data["choices"][0]["message"]["content"]

    except Exception as e:
        print("LLM ERROR:", e)
        return "Something went wrong with LLM"