from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def voice_selection_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="🇷🇺 Дмитрий", callback_data="ru_male_1"),
                InlineKeyboardButton(text="🇷🇺 Светлана", callback_data="ru_female_1"),
            ],
            [
                InlineKeyboardButton(text="🇬🇧 Guy", callback_data="en_male_us"),
                InlineKeyboardButton(text="🇬🇧 Jenny", callback_data="en_female_us"),
            ],
            [
                InlineKeyboardButton(text="🇩🇪 Conrad", callback_data="de_male"),
                InlineKeyboardButton(text="🇩🇪 Katja", callback_data="de_female"),
            ],
            [
                InlineKeyboardButton(text="🇺🇿 Sardor", callback_data="uz_male"),
                InlineKeyboardButton(text="🇺🇿 Madina", callback_data="uz_female"),
            ],
        ]
    )
