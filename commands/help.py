from telegram import Update
from telegram.ext import ContextTypes

async def call_help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Type /coin, /dice or /magicball to get an answer')
