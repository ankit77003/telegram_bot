import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
from dotenv import load_dotenv
from llm import get_llm_response
from db import store_message

load_dotenv()

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        print("Message received")
        user_msg = update.message.text
        user_id = str(update.message.from_user.id)

        # LLM reply
        bot_reply = get_llm_response(user_msg)

        # store message safely
        try:
            store_message(user_id, user_msg, bot_reply)
        except Exception as e:
            print("DB ERROR:", e)

        # reply to user
        await update.message.reply_text(bot_reply)

    except Exception as e:
        print("BOT ERROR:", e)
        await update.message.reply_text("Something went wrong 😅")

# build Telegram app
app = ApplicationBuilder().token(os.getenv("TELEGRAM_TOKEN")).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

app.run_polling()