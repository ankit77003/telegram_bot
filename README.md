# Telegram LLM Bot

A Telegram bot that uses an LLM (OpenAI or OpenRouter) to respond to messages and stores all conversations in Supabase.

---

## Features

- Receive messages from Telegram users  
- Send messages to an LLM (GPT-3.5 or GPT-4 via OpenAI/OpenRouter)  
- Store every conversation turn (user + bot) in a Supabase table  
- Handle API errors gracefully (quota exceeded, network issues)  
- Can run 24/7 (locally or on a server)

---

## Tech Stack

- **Python 3.9+**  
- **Telegram Bot API** via `python-telegram-bot`  
- **LLM API** (OpenAI or OpenRouter)  
- **Supabase** for storing messages  
- **dotenv** for environment variables  

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/telegram_bot.git
cd telegram_bot
