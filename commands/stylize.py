from telegram import Update
from telegram.ext import ContextTypes

from lang_utils import get_user_language
from languages import get_text

async def stylize(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    lang = get_user_language(user_id)

    text = get_text(lang, "send_image")

    await update.message.reply_text(text)
    context.user_data['awaiting_image'] = True