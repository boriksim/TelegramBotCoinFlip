import requests
import config
from telegram import Update
from telegram.ext import ContextTypes

from lang_utils import get_user_language
from languages import get_text

API_URL = "https://api.thedogapi.com/v1/images/search"
DOG_API_KEY = config.DOG_API_KEY

async def dog(update: Update, context: ContextTypes.DEFAULT_TYPE):
    headers = {"x-api-key": DOG_API_KEY}

    user_id = update.effective_user.id
    lang = get_user_language(user_id)

    dog_not_found = get_text(lang, "dog_not_found")

    try:
        response = requests.get(API_URL, headers=headers, timeout=5)
        response.raise_for_status()
        data = response.json()

        if not data or 'url' not in data[0]:
            raise ValueError("Invalid response structure")

        dog_url = data[0]['url']
        await context.bot.send_photo(chat_id=update.effective_chat.id, photo=dog_url)

    except Exception as error:
        print("Error getting cat image:", error)
        await update.message.reply_text(dog_not_found)