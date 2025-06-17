from magicball_responses import responses

LANG = {
    "en": {
        "start": "Welcome! Choose an option:",
        "coinflip": "Coinflip",
        "d6": "Roll D6",
        "magicball": "Ask Magic Ball",
        "coin_text": "It\'s",
        "heads": "Heads",
        "tails": "Tails",
        "dice": "You rolled a:",
        "magicball_text": "Magicball says: ",
        "help": "Type /coin /dice /magicball",
        "flipping_coin": "Flipping coin...",
        "rolling_dice": "Rolling dice...",
        "asking_magicball": "Asking Magicball...",
        "responses": [
            "It is certain.",
            "It is decidedly so.",
            "Without a doubt.",
            "Yes – definitely.",
            "You may rely on it.",
            "As I see it, yes.",
            "Most likely.",
            "Outlook good.",
            "Yes.",
            "Signs point to yes.",
            "Reply hazy, try again.",
            "Ask again later.",
            "Better not tell you now.",
            "Cannot predict now.",
            "Concentrate and ask again.",
            "Don't count on it.",
            "My reply is no.",
            "My sources say no.",
            "Outlook not so good.",
            "Very doubtful."
        ]

    },
    "ru": {
        "start": "Добро пожаловать! Выберите опцию:",
        "coinflip": "Монетка",
        "d6": "Шестигранник",
        "magicball": "Магический Шар",
        "coin_text": "Выпал",
        "heads": "Орел",
        "tails": "Решка",
        "dice": "Выпало:",
        "magicball_text": "Магический шар говорит: ",
        "help": "Напечатайте /coin /dice /magicball",
        "flipping_coin": "Подбрасываю монетку...",
        "rolling_dice": "Бросаю кубик...",
        "asking_magicball": "Спрашиваю магический шар...",
        "responses": [
            "Это несомненно.",
            "Безусловно, так.",
            "Без сомнения.",
            "Да – определённо.",
            "Можешь на это положиться.",
            "Как я вижу, да.",
            "Скорее всего.",
            "Перспективы хорошие.",
            "Да.",
            "Знаки указывают на да.",
            "Ответ неясен, попробуй снова.",
            "Спроси позже.",
            "Лучше не говорить тебе сейчас.",
            "Сейчас предсказать невозможно.",
            "Сосредоточься и спроси снова.",
            "Не рассчитывай на это.",
            "Мой ответ — нет.",
            "Мои источники говорят нет.",
            "Перспективы не очень хорошие.",
            "Очень сомнительно."
        ]

    }
}

def get_text(lang, key):
    return LANG.get(lang, LANG["en"]).get(key, "language error")
