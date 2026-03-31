Telegram LLM Bot

A Telegram bot that uses an LLM (OpenAI or OpenRouter) to respond to messages and stores all conversations in Supabase.

Features
Receives messages from Telegram users.
Sends messages to an LLM (GPT-3.5 or GPT-4 via OpenAI/OpenRouter).
Stores every conversation turn (user + bot) in a Supabase table.
Handles API errors gracefully (quota exceeded, network issues).
Can run 24/7 (with server or background process).
Tech Stack
Python 3.9+
Telegram Bot API via python-telegram-bot
LLM API (OpenAI or OpenRouter)
Supabase for storing messages
dotenv for environment variables
Setup Instructions
1. Clone the repository
git clone https://github.com/yourusername/telegram_bot.git
cd telegram_bot
2. Create a virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
3. Install dependencies
pip install -r requirements.txt

requirements.txt should include:

python-telegram-bot==20.3
requests
python-dotenv
supabase
4. Create .env file
TELEGRAM_TOKEN=your_telegram_bot_token
OPENROUTER_API_KEY=your_openrouter_api_key
SUPABASE_URL=https://your-supabase-project-url.supabase.co
SUPABASE_KEY=your_supabase_anon_key

Replace the placeholders with your own keys.

5. Set up Supabase table

Create a table messages with columns:

Column	Type
user_id	text
user_message	text
bot_response	text

Important: Either turn off Row-Level Security (RLS) for testing or add a policy to allow inserts for your key.

6. Run the bot locally
python3 bot.py
Open Telegram → message your bot → you should see replies.
Check Supabase → new rows appear for every conversation.
7. Run 24/7 (Optional)

macOS/Linux:

nohup python3 bot.py &

Windows:

start /b python bot.py

Cloud hosting: Use Railway, Replit, or AWS for always-on bot.

Error Handling
If LLM API fails (quota exceeded), the bot replies with a fallback message.
DB insert errors are logged but won’t crash the bot.
License

MIT License – feel free to use and modify.
