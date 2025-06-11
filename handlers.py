import random
from inline_keyboard import get_repeat_keyboard
import magicball_responses

from telegram import Update, ReplyKeyboardRemove, ReplyKeyboardMarkup
from telegram.ext import ContextTypes

from config import BOT_USERNAME

import commands as cmd


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


async def handle_keyboard_input(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    remove_keyboard = ReplyKeyboardRemove()

    if text == "Coinflip":
        await update.message.reply_text("Flipping the coin...", reply_markup=remove_keyboard)
        await cmd.coin(update, context)
    elif text == "Roll D6":
        await update.message.reply_text("Rolling the dice...", reply_markup=remove_keyboard)
        await cmd.dice(update, context)
    elif text == "Ask Magic Ball":
        await update.message.reply_text("Asking the Magic Ball...", reply_markup=remove_keyboard)
        await cmd.magicball(update, context)
    else:
        await update.message.reply_text("Please choose an option from the keyboard.")


async def handle_inline_keyboard(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "repeat_coin":
        await context.bot.send_message(chat_id=query.message.chat.id,
                                       text=f"It\'s <i>{random.choice(['heads', 'tails'])}</i>!", parse_mode='HTML',
                                       reply_markup=get_repeat_keyboard("coin"))
    elif query.data == "repeat_dice":
        await context.bot.send_message(chat_id=query.message.chat.id,
                                       text=f"You rolled a <b>{random.randint(1, 6)}</b>", parse_mode='HTML',
                                       reply_markup=get_repeat_keyboard("dice"))
    elif query.data == "repeat_magicball":
        await context.bot.send_message(chat_id=query.message.chat.id,
                                       text=f"The magic ball says: <i>{random.choice(magicball_responses.responses)}</i>",
                                       parse_mode='HTML', reply_markup=get_repeat_keyboard("magicball"))
    elif query.data == "start_menu":
        menu_keyboard = [["Coinflip", "Roll D6", "Ask Magic Ball"]]
        reply_markup = ReplyKeyboardMarkup(menu_keyboard, resize_keyboard=True)
        await context.bot.send_message(chat_id=query.message.chat.id, text="Hello, choose an option below!",
                                       reply_markup=reply_markup)


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')
