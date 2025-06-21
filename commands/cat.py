import requests
import config
from telegram import Update
from telegram.ext import ContextTypes

from lang_utils import get_user_language
from languages import get_text

API_URL = "https://api.thecatapi.com/v1/images/search"
CAT_API_KEY = config.CAT_API_KEY

async def cat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    headers = {"x-api-key": CAT_API_KEY}

    user_id = update.effective_user.id
    lang = get_user_language(user_id)

    cat_not_found = get_text(lang, "cat_not_found")

    try:
        response = requests.get(API_URL, headers=headers, timeout=5)
        response.raise_for_status()
        data = response.json()

        if not data or 'url' not in data[0]:
            raise ValueError("Invalid response structure")

        cat_url = data[0]['url']
        await context.bot.send_photo(chat_id=update.effective_chat.id, photo=cat_url)

    except Exception as error:
        print("Error getting cat image:", error)
        await update.message.reply_text(cat_not_found)