from telegram.ext import Application, CommandHandler, MessageHandler, CallbackQueryHandler, filters, ContextTypes

from dotenv import load_dotenv

load_dotenv()

import lang_utils

import config

import commands as cmd
from handlers import handle_message, error, handle_keyboard_input, handle_inline_keyboard, handle_lang, handle_image

if __name__ == '__main__':
    print('Starting coinflip bot...')
    app = Application.builder().token(config.BOT_TOKEN).build()

    app.add_handler(CommandHandler('start', cmd.start))
    app.add_handler(CommandHandler('help', cmd.call_help))
    app.add_handler(CommandHandler('coin', cmd.coin))
    app.add_handler(CommandHandler('dice', cmd.dice))
    app.add_handler(CommandHandler('magicball', cmd.magicball))
    app.add_handler(CommandHandler('cat', cmd.cat))
    app.add_handler(CommandHandler('dog', cmd.dog))

    app.add_handler(CommandHandler("stylize", cmd.stylize))
    app.add_handler(MessageHandler(filters.PHOTO, handle_image))

    app.add_handler(CommandHandler('lang', cmd.lang))
    app.add_handler(CallbackQueryHandler(handle_lang, pattern=r'^lang_'))

    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_keyboard_input))
    app.add_handler(CallbackQueryHandler(handle_inline_keyboard))
    app.add_handler(MessageHandler(filters.TEXT, handle_message))
    app.add_error_handler(error)

    # Polls the bot
    print('Polling...')
    app.run_polling(poll_interval=1)
