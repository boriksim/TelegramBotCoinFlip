import random
from inline_keyboard import get_repeat_keyboard

from telegram import Update
from telegram.ext import ContextTypes

from lang_utils import get_user_language
from languages import get_text

async def coin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    lang = get_user_language(user_id)

    coin_text = get_text(lang, "coin_text")
    heads = get_text(lang, "heads")
    tails = get_text(lang, "tails")

    await update.message.reply_text(f"{coin_text} <i>{random.choice([heads, tails])}</i>!", parse_mode='HTML',
                                    reply_markup=get_repeat_keyboard("coin"))
