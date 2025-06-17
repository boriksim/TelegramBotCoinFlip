from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

from lang_utils import set_user_language, get_user_language

LANG_BUTTONS = InlineKeyboardMarkup([
    [InlineKeyboardButton("English", callback_data='lang_en')],
    [InlineKeyboardButton("Русский", callback_data='lang_ru')]
])

async def lang(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Choose your language / Выберите язык:", reply_markup=LANG_BUTTONS)
