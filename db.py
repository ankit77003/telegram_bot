from supabase import create_client
from dotenv import load_dotenv
import os

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

    response = supabase.table("messages").insert(data).execute()
    return response