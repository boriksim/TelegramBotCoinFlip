# Telegram Coin Bot

This is a simple Telegram bot written in Python:

## 🤖 Available Commands

- `/start` — Launches the bot and sends a welcome message.  
- `/help` — Shows available commands and what the bot can do.  
- `/coin` — Flips a coin and returns a random result: **heads** or **tails**.
- `/dice` — Rolls a 6 sided dice.
- `/magicball` — Prints a random Magic 8 Ball response.
- `/cat` — Sends a random cat photo.
- `/dog` — Sends a random dog photo.
- `/lang` — Choice of user language.
- `/stylize` — Redaction of your image.

---

## ⚙️ Configuration

To run the bot, you need to create a configuration file.

1. **Create a file named** `.env` in the project directory.

2. **Paste the following content** into `.env`, replacing the placeholders:

```python
# .env

TOKEN = "your_telegram_bot_token"           #provided by BotFather
BOT_USERNAME = "your_telegram_bot_username" #username when creating your bot
APP_NAME = "your_app_name"                  #if you are using webhooks
MODE = "working_mode"                       #"polling" for polling, "webhook" for webhook
CAT_API_KEY = "your_cat_api_key"            #https://thecatapi.com/
DOG_API_KEY = "your_dog_api_jey"            #https://thedogapi.com/
