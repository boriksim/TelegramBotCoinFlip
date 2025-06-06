import os
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from commands import start_command, help_command, coin_command, dice_command, magicball_command
from handlers import handle_message, error

BOT_TOKEN = os.environ.get("BOT_TOKEN")
APP_NAME = os.environ.get("APP_NAME")

WEBHOOK_PATH = f"/{BOT_TOKEN}"
WEBHOOK_URL = f"https://{APP_NAME}.onrender.com{WEBHOOK_PATH}"

async def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("coin", coin_command))
    app.add_handler(CommandHandler("dice", dice_command))
    app.add_handler(CommandHandler("magicball", magicball_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.add_error_handler(error)

    await app.bot.set_webhook(WEBHOOK_URL)

    await app.run_webhook(
        listen="0.0.0.0",
        port=int(os.environ.get("PORT", 8443)),
        webhook_url=WEBHOOK_URL,
    )

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
