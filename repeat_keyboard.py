from telegram import InlineKeyboardMarkup, InlineKeyboardButton

def get_repeat_keyboard(command: str) -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton("Repeat", callback_data=f"repeat_{command}"),
            InlineKeyboardButton("Menu", callback_data="start_menu"),
        ]
    ]
    return InlineKeyboardMarkup(keyboard)
