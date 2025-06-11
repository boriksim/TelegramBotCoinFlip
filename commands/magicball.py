import random
import magicball_responses

from telegram import Update
from telegram.ext import ContextTypes

from inline_keyboard import get_repeat_keyboard

async def magicball(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"The magic ball says: <i>{random.choice(magicball_responses.responses)}</i>", parse_mode='HTML', reply_markup=get_repeat_keyboard("magicball"))
