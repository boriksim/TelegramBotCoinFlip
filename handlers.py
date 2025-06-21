import random
from inline_keyboard import get_repeat_keyboard

from telegram import Update, ReplyKeyboardRemove, ReplyKeyboardMarkup
from telegram.ext import ContextTypes

from config import BOT_USERNAME

from lang_utils import get_user_language, set_user_language
from languages import get_text

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

    user_id = update.effective_user.id
    lang = get_user_language(user_id)

    flipping_coin = get_text(lang, "flipping_coin")
    rolling_dice = get_text(lang, "rolling_dice")
    asking_magicball = get_text(lang, "asking_magicball")
    choose_option = get_text(lang, "start")

    if text == "Coinflip":
        await update.message.reply_text(flipping_coin, reply_markup=remove_keyboard)
        await cmd.coin(update, context)
    elif text == "Roll D6":
        await update.message.reply_text(rolling_dice, reply_markup=remove_keyboard)
        await cmd.dice(update, context)
    elif text == "Ask Magic Ball":
        await update.message.reply_text(asking_magicball, reply_markup=remove_keyboard)
        await cmd.magicball(update, context)
    else:
        await update.message.reply_text(choose_option)


async def handle_inline_keyboard(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    user_id = update.effective_user.id
    lang = get_user_language(user_id)

    coin_text = get_text(lang, "coin_text")
    heads = get_text(lang, "heads")
    tails = get_text(lang, "tails")
    dice_text = get_text(lang, "dice")
    magicball_text = get_text(lang, "magicball_text")
    responses = get_text(lang, "responses")
    start_text = get_text(lang, "start")

    if query.data == "repeat_coin":
        await context.bot.send_message(chat_id=query.message.chat.id,
                                       text=f"{coin_text} <i>{random.choice([heads, tails])}</i>!", parse_mode='HTML',
                                       reply_markup=get_repeat_keyboard("coin"))
    elif query.data == "repeat_dice":
        await context.bot.send_message(chat_id=query.message.chat.id,
                                       text=f"{dice_text} <b>{random.randint(1, 6)}</b>", parse_mode='HTML',
                                       reply_markup=get_repeat_keyboard("dice"))
    elif query.data == "repeat_magicball":
        await context.bot.send_message(chat_id=query.message.chat.id,
                                       text=f"{magicball_text} <i>{random.choice(responses)}</i>",
                                       parse_mode='HTML', reply_markup=get_repeat_keyboard("magicball"))
    elif query.data == "start_menu":
        menu_keyboard = [["Coinflip", "Roll D6", "Ask Magic Ball"]]
        reply_markup = ReplyKeyboardMarkup(menu_keyboard, resize_keyboard=True)
        await context.bot.send_message(chat_id=query.message.chat.id, text=start_text,
                                       reply_markup=reply_markup)


async def handle_lang(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    user_id = query.from_user.id
    lang_code = query.data.split('_')[1]
    set_user_language(user_id, lang_code)

    if lang_code == "en":
        text = "Language updated!"
    elif lang_code == "pl":
        text = "Język został zaktualizowany!"
    elif lang_code == "ru":
        text = "Язык обновлен!"
    else:
        text = "Language error"

    await query.edit_message_text(text)


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')
