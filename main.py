from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

from dotenv import load_dotenv

load_dotenv()

import config
from config import BOT_USERNAME

from commands import start, call_help, coin, dice, magicball


# Responses

def handle_response(text: str) -> str:
    processed: str = text.lower()
    if 'aboba' in processed:
        return 'aboba'
    return 'I don\'t understand that, please type /coin, /dice or /magicball to get an answer'


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        response: str = handle_response(text)

    print('Bot:', response)
    await update.message.reply_text(response)


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')


if __name__ == '__main__':
    print('Starting coinflip bot...')
    app = Application.builder().token(config.BOT_TOKEN).build()

    # Commands
    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('help', call_help))
    app.add_handler(CommandHandler('coin', coin))
    app.add_handler(CommandHandler('dice', dice))
    app.add_handler(CommandHandler('magicball', magicball))

    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Errors
    app.add_error_handler(error)

    # Polls the bot
    print('Polling...')
    app.run_polling(poll_interval=1)
