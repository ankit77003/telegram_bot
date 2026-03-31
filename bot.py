# bot.py
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
import os
from llm import get_llm_response
from db import store_message
from dotenv import load_dotenv

load_dotenv()

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("Message received") 
    user_msg = update.message.text
    user_id = str(update.message.from_user.id)

    # Call LLM
    bot_reply = get_llm_response(user_msg)

    # Store in DB
    store_message(user_id, user_msg, bot_reply)

    # Reply to user
    await update.message.reply_text(bot_reply)

app = ApplicationBuilder().token(os.getenv("TELEGRAM_TOKEN")).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

app.run_polling()