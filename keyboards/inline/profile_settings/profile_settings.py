from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

from keyboards.inline.profile_settings.callback_datas import age_callback_data, earning_callback_data

change_personal_info_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Пройти анкету", callback_data="settings")
        ]
    ]
)

select_age_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="12-18", callback_data=age_callback_data.new(age="12-18")),
            InlineKeyboardButton(text="19-24", callback_data=age_callback_data.new(age="18-24")),
        ],
        [
            InlineKeyboardButton(text="25-27", callback_data=age_callback_data.new(age="25-27")),
            InlineKeyboardButton(text="28+",   callback_data=age_callback_data.new(age="28+")),
        ],
    ]
)

get_location_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Отправить геопозицию", request_location=True)
        ]
    ]
)

has_earning_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            KeyboardButton(text="Да, я зарабатываю сам и лично распоряжаюсь своими финансами",
                           callback_data=earning_callback_data.new(has_earning=True)),
            KeyboardButton(text="Нет, живу на средства родителей",
                           callback_data=earning_callback_data.new(has_earning=False)),
        ],
    ]
)