# Telegram Coin Bot

This is a simple Telegram bot written in Python:

## 🤖 Available Commands

- `/start` — Launches the bot and sends a welcome message.  
- `/help` — Shows available commands and what the bot can do.  
- `/coin` — Flips a coin and returns a random result: **heads** or **tails**.

---

## ⚙️ Configuration

To run the bot, you need to create a configuration file with your Telegram bot token and username.

1. **Create a file named** `config.py` in the project directory.

2. **Paste the following content** into `config.py`, replacing the placeholders:

```python
# config.py

TOKEN = "your_telegram_bot_token"
BOT_USERNAME = "your_telegram_bot_username"
