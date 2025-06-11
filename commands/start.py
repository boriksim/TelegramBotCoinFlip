from telegram import Update, ReplyKeyboardMarkup, InlineKeyboardMarkup
from telegram.ext import ContextTypes

from commands import coin, dice, magicball

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    menu_keyboard = [["Coinflip", "Roll D6", "Ask Magic Ball"]]

    reply_markup = ReplyKeyboardMarkup(menu_keyboard, resize_keyboard=True)

    await update.message.reply_text("Hello, choose an option below!", reply_markup=reply_markup)