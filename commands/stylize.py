from telegram import Update
from telegram.ext import ContextTypes

from lang_utils import get_user_language
from languages import get_text

async def stylize(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Send me an image to redact")
    context.user_data['awaiting_image'] = True