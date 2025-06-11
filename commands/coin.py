import random
from inline_keyboard import get_repeat_keyboard

from telegram import Update
from telegram.ext import ContextTypes


async def coin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"It\'s <i>{random.choice(['heads', 'tails'])}</i>!", parse_mode='HTML',
                                    reply_markup=get_repeat_keyboard("coin"))
