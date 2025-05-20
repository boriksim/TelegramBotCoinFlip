import random

from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

async def coin_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"It\'s <i>{random.choice(['heads', 'tails'])}</i>!", parse_mode='HTML')