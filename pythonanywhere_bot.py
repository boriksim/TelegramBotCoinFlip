import random

from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

import config
from config import BOT_USERNAME


# Commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello, type /coin, /dice or /magicball!')


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Type /coin, /dice or /magicball to get an answer')


async def coin_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"It\'s <i>{random.choice(['heads', 'tails'])}</i>!", parse_mode='HTML')


async def dice_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"You rolled a <b>{random.randint(1, 6)}</b>", parse_mode='HTML')


responses = ["It is certain.", "It is decidedly so.", "Without a doubt.", "Yes – definitely.", "You may rely on it.",
             "As I see it, yes.", "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.",
             "Reply hazy, try again.", "Ask again later.", "Better not tell you now.", "Cannot predict now.",
             "Concentrate and ask again.", "Don't count on it.", "My reply is no.", "My sources say no.",
             "Outlook not so good.", "Very doubtful."]


async def magicball_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"The magic ball says: <i>{random.choice(responses)}</i>", parse_mode='HTML')


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
    app = Application.builder().token(config.TOKEN).build()

    # Commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('coin', coin_command))
    app.add_handler(CommandHandler('dice', dice_command))
    app.add_handler(CommandHandler('magicball', magicball_command))

    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Errors
    app.add_error_handler(error)

    # Polls the bot
    print('Polling...')
    app.run_polling(poll_interval=1)
