import os
import random
from inline_keyboard import get_repeat_keyboard

from telegram import Update, ReplyKeyboardRemove, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

from PIL import Image, ImageOps, ImageFilter

from config import BOT_USERNAME

from lang_utils import get_user_language, set_user_language
from languages import get_text

import commands as cmd

def handle_response(text: str) -> str:
    processed: str = text.lower()
    if 'aboba' in processed:
        return 'aboba'
    return 'I don\'t understand that, please type /coin, /dice or /magicball to get an answer'


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        response: str = handle_response(text)

    print('Bot:', response)
    await update.message.reply_text(response)


async def handle_keyboard_input(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    remove_keyboard = ReplyKeyboardRemove()

    user_id = update.effective_user.id
    lang = get_user_language(user_id)

    flipping_coin = get_text(lang, "flipping_coin")
    rolling_dice = get_text(lang, "rolling_dice")
    asking_magicball = get_text(lang, "asking_magicball")
    choose_option = get_text(lang, "start")

    if text == "Coinflip":
        await update.message.reply_text(flipping_coin, reply_markup=remove_keyboard)
        await cmd.coin(update, context)
    elif text == "Roll D6":
        await update.message.reply_text(rolling_dice, reply_markup=remove_keyboard)
        await cmd.dice(update, context)
    elif text == "Ask Magic Ball":
        await update.message.reply_text(asking_magicball, reply_markup=remove_keyboard)
        await cmd.magicball(update, context)
    else:
        await update.message.reply_text(choose_option)


async def handle_image(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.user_data.get('awaiting_image'):
        image = update.message.photo[-1]
        file = await context.bot.get_file(image.file_id)

        os.makedirs("images", exist_ok=True)
        file_path = f"images/{update.effective_user.id}_original.jpg"
        await file.download_to_drive(file_path)

        context.user_data['awaiting_image'] = False
        context.user_data['image_path'] = file_path

        keyboard = [
            [InlineKeyboardButton("🎨 Color", callback_data="color_menu"),
             InlineKeyboardButton("📐 Rotate", callback_data="rotate_menu"),
             InlineKeyboardButton("🌀 Filters", callback_data="filters_menu")],
            [InlineKeyboardButton("❌ Cancel", callback_data="cancel")]
        ]

        await update.message.reply_text("Choose the action to perform on the image",
                                        reply_markup=InlineKeyboardMarkup(keyboard))


async def handle_inline_keyboard(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    user_id = update.effective_user.id
    lang = get_user_language(user_id)

    coin_text = get_text(lang, "coin_text")
    heads = get_text(lang, "heads")
    tails = get_text(lang, "tails")
    dice_text = get_text(lang, "dice")
    magicball_text = get_text(lang, "magicball_text")
    responses = get_text(lang, "responses")
    start_text = get_text(lang, "start")

    if query.data == "repeat_coin":
        await context.bot.send_message(chat_id=query.message.chat.id,
                                       text=f"{coin_text} <i>{random.choice([heads, tails])}</i>!", parse_mode='HTML',
                                       reply_markup=get_repeat_keyboard("coin"))
    elif query.data == "repeat_dice":
        await context.bot.send_message(chat_id=query.message.chat.id,
                                       text=f"{dice_text} <b>{random.randint(1, 6)}</b>", parse_mode='HTML',
                                       reply_markup=get_repeat_keyboard("dice"))
    elif query.data == "repeat_magicball":
        await context.bot.send_message(chat_id=query.message.chat.id,
                                       text=f"{magicball_text} <i>{random.choice(responses)}</i>",
                                       parse_mode='HTML', reply_markup=get_repeat_keyboard("magicball"))
    elif query.data == "start_menu":
        menu_keyboard = [["Coinflip", "Roll D6", "Ask Magic Ball"]]
        reply_markup = ReplyKeyboardMarkup(menu_keyboard, resize_keyboard=True)
        await context.bot.send_message(chat_id=query.message.chat.id, text=start_text,
                                       reply_markup=reply_markup)


    elif query.data == "cancel":
        await query.edit_message_text("Redaction canceled")
    elif query.data == "color_menu":
        keyboard = [
            [InlineKeyboardButton("Black&White", callback_data="redact_b&w")],
            [InlineKeyboardButton("Invert", callback_data="redact_invert")],
            [InlineKeyboardButton("← Return", callback_data="image_menu")]
        ]
        await query.edit_message_text("Color effects:", reply_markup=InlineKeyboardMarkup(keyboard))
    elif query.data == "rotate_menu":
        keyboard = [
            [InlineKeyboardButton("90 degrees counter clockwise", callback_data="redact_rotate_90_CC")],
            [InlineKeyboardButton("90 degrees clockwise", callback_data="redact_rotate_90_C")],
            [InlineKeyboardButton("180 degrees", callback_data="redact_rotate_180")],
            [InlineKeyboardButton("← Return", callback_data="image_menu")]
        ]
        await query.edit_message_text("Rotation options:", reply_markup=InlineKeyboardMarkup(keyboard))
    elif query.data == "filters_menu":
        keyboard = [
            [InlineKeyboardButton("Blur", callback_data="redact_filter_blur"),
             InlineKeyboardButton("Contour", callback_data="redact_filter_contour"),
             InlineKeyboardButton("Detail", callback_data="redact_filter_detail"),],
            [InlineKeyboardButton("Edge enchance", callback_data="redact_filter_edge_enchance"),
             InlineKeyboardButton("Emboss", callback_data="redact_filter_emboss"),
             InlineKeyboardButton("Find edges", callback_data="redact_filter_find_deges"),],
            [InlineKeyboardButton("← Return", callback_data="image_menu")]
        ]
        await query.edit_message_text("Filter effects:", reply_markup=InlineKeyboardMarkup(keyboard))
    elif query.data == "image_menu":
        keyboard = [
            [InlineKeyboardButton("🎨 Color", callback_data="color_menu")],
            [InlineKeyboardButton("📐 Rotate", callback_data="rotate_menu")],
            [InlineKeyboardButton("🌀 Filters", callback_data="filters_menu")],
            [InlineKeyboardButton("❌ Cancel", callback_data="cancel")]
        ]
        await context.bot.send_message(chat_id=query.message.chat.id, text="Choose the action to perform on the image",
                                       reply_markup=InlineKeyboardMarkup(keyboard))

    elif query.data[:7] == "redact_":
        image_path = context.user_data.get('image_path')
        if not image_path or not os.path.exists(image_path):
            await query.edit_message_text("Image not found")

        processed_path = f"images/{update.effective_user.id}_processed.jpg"
        image = Image.open(image_path)

        if query.data == "redact_b&w":
            image = image.convert("L")
        elif query.data == "redact_invert":
            image = ImageOps.invert(image.convert("RGB"))

        elif query.data == "redact_rotate_90_CC":
            image = image.rotate(angle=90, expand=True)
        elif query.data == "redact_rotate_90_C":
            image = image.rotate(angle=-90, expand=True)
        elif query.data == "redact_rotate_180":
            image = image.rotate(angle=180, expand=True)

        elif query.data == "redact_filter_blur":
            image = image.filter(ImageFilter.GaussianBlur(radius=10))
        elif query.data == "redact_filter_contour":
            image = image.filter(ImageFilter.CONTOUR)
        elif query.data == "redact_filter_detail":
            image = image.filter(ImageFilter.DETAIL)
        elif query.data == "redact_filter_edge_enchance":
            image = image.filter(ImageFilter.EDGE_ENHANCE)
        elif query.data == "redact_filter_emboss":
            image = image.filter(ImageFilter.EMBOSS)
        elif query.data == "redact_filter_find_edges":
            image = image.filter(ImageFilter.FIND_EDGES)


        image.save(processed_path)
        await context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(processed_path, "rb"),
                                     caption=f"Here is your redacted image")


async def handle_lang(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    user_id = query.from_user.id
    lang_code = query.data.split('_')[1]
    set_user_language(user_id, lang_code)

    if lang_code == "en":
        text = "Language updated!"
    elif lang_code == "pl":
        text = "Język został zaktualizowany!"
    elif lang_code == "ru":
        text = "Язык обновлен!"
    else:
        text = "Language error"

    await query.edit_message_text(text)


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')
