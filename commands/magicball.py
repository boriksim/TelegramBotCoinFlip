import random
import magicball_responses

from telegram import Update
from telegram.ext import ContextTypes

from inline_keyboard import get_repeat_keyboard

from lang_utils import get_user_language
from languages import get_text

async def magicball(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    lang = get_user_language(user_id)

    text = get_text(lang, "magicball_text")
    responses = get_text(lang, "responses")

    await update.message.reply_text(f"{text} <i>{random.choice(responses)}</i>", parse_mode='HTML', reply_markup=get_repeat_keyboard("magicball"))
