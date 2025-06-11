import random
from inline_keyboard import get_repeat_keyboard

from telegram import Update
from telegram.ext import ContextTypes


async def dice(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"You rolled a <b>{random.randint(1, 6)}</b>", parse_mode='HTML',
                                    reply_markup=get_repeat_keyboard("dice"))
