import os
from supabase import create_client
from dotenv import load_dotenv

load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

supabase = create_client(url, key)

def store_message(user_id, user_message, bot_response):
    data = {
        "user_id": user_id,
        "user_message": user_message,
        "bot_response": bot_response
    }
    try:
        response = supabase.table("messages").insert(data).execute()
        print("DB insert done:", response)
        return response
    except Exception as e:
        print("DB ERROR:", e)
        return None