import random
from inline_keyboard import get_repeat_keyboard

from telegram import Update
from telegram.ext import ContextTypes

from lang_utils import get_user_language
from languages import get_text


async def dice(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    lang = get_user_language(user_id)

    dice = get_text(lang, "dice")

    await update.message.reply_text(f"{dice} <b>{random.randint(1, 6)}</b>", parse_mode='HTML',
                                    reply_markup=get_repeat_keyboard("dice"))
