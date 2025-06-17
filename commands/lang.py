from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

LANG_BUTTONS = InlineKeyboardMarkup([
    [InlineKeyboardButton("English", callback_data='lang_en')],
    [InlineKeyboardButton("Русский", callback_data='lang_ru')],
    [InlineKeyboardButton("Polska", callback_data='lang_pl')],
])

async def lang(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Choose your language / Выберите язык / Wybierz język:", reply_markup=LANG_BUTTONS)
