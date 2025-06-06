import os
from flask import Flask, request

from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

import config

from commands import start_command, help_command, coin_command, dice_command, magicball_command
from handlers import handle_message, error

app = Flask(__name__)
telegram_app = Application.builder().token(config.BOT_TOKEN).build()

telegram_app.add_handler(CommandHandler('start', start_command))
telegram_app.add_handler(CommandHandler('help', help_command))
telegram_app.add_handler(CommandHandler('coin', coin_command))
telegram_app.add_handler(CommandHandler('dice', dice_command))
telegram_app.add_handler(CommandHandler('magicball', magicball_command))
telegram_app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
telegram_app.add_error_handler(error)


@app.post(f"/{config.BOT_TOKEN}")
async def webhook():
    update = Update.de_json(request.get_json(force=True), telegram_app.bot)
    await telegram_app.process_update(update)
    return "OK", 200


@app.get('/set_webhook')
async def set_webhook():
    url = f"https://{config.APP_NAME}.onrender.com/{config.BOT_TOKEN}"
    await telegram_app.bot.set_webhook(url)
    return f"Webhook set to {url}", 200

@app.get("/")
def home():
    return "Bot is up!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

port = int(os.environ.get('PORT', 10000))
app.run(host="0.0.0.0", port=port)
