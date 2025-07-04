import os
from flask import Flask, request

from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackQueryHandler, filters, ContextTypes

from dotenv import load_dotenv

load_dotenv()

import config

import commands as cmd
from handlers import handle_message, error, handle_keyboard_input, handle_inline_keyboard, handle_lang, handle_image

app = Flask(__name__)
telegram_app = Application.builder().token(config.BOT_TOKEN).build()

telegram_app.add_handler(CommandHandler('start', cmd.start))
telegram_app.add_handler(CommandHandler('help', cmd.call_help))
telegram_app.add_handler(CommandHandler('coin', cmd.coin))
telegram_app.add_handler(CommandHandler('dice', cmd.dice))
telegram_app.add_handler(CommandHandler('magicball', cmd.magicball))
telegram_app.add_handler(CommandHandler('cat', cmd.cat))
telegram_app.add_handler(CommandHandler('dog', cmd.dog))

telegram_app.add_handler(CommandHandler("stylize", cmd.stylize))
telegram_app.add_handler(MessageHandler(filters.PHOTO, handle_image))

telegram_app.add_handler(CommandHandler('lang', cmd.lang))
telegram_app.add_handler(CallbackQueryHandler(handle_lang, pattern=r'^lang_'))

telegram_app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_keyboard_input))
telegram_app.add_handler(CallbackQueryHandler(handle_inline_keyboard))
telegram_app.add_handler(MessageHandler(filters.TEXT, handle_message))
telegram_app.add_error_handler(error)


@app.post(f"/{config.BOT_TOKEN}")
async def webhook():
    await telegram_app.initialize()
    update = Update.de_json(request.get_json(force=True), telegram_app.bot)
    await telegram_app.process_update(update)
    return "OK", 200


@app.get('/set_webhook')
async def set_webhook():
    url = f"https://{config.APP_NAME}.onrender.com/{config.BOT_TOKEN}"
    await telegram_app.initialize()
    await telegram_app.bot.set_webhook(url)
    return f"Webhook set to {url}", 200


@app.get("/")
def home():
    return "Bot is up!"


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 10000))
    app.run(host="0.0.0.0", port=port)
