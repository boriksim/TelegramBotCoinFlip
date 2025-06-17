from telegram import Update
from telegram.ext import ContextTypes

from lang_utils import get_user_language
from languages import get_text

async def call_help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    lang = get_user_language(user_id)

    help_text = get_text(lang, "help")

    await update.message.reply_text(help_text)
