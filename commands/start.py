from telegram import Update, ReplyKeyboardMarkup, InlineKeyboardMarkup
from telegram.ext import ContextTypes

from lang_utils import get_user_language
from languages import get_text

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    lang = get_user_language(user_id)

    welcome = get_text(lang, "start")

    menu_keyboard = [["Coinflip", "Roll D6", "Ask Magic Ball"]]

    reply_markup = ReplyKeyboardMarkup(menu_keyboard, resize_keyboard=True)

    await update.message.reply_text(welcome, reply_markup=reply_markup)