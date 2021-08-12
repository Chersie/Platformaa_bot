from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from .callback_datas import read_faq_callback_data

faq_start_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="📖 Прочитать FAQ", callback_data=read_faq_callback_data.new(want_to_read="Yes")),
            InlineKeyboardButton(text="Разберусь походу", callback_data=read_faq_callback_data.new(want_to_read="No"))
        ]
    ]
)

faq_continue_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="⏩ Понятно!\nПродолжить", callback_data="faq_readed"),
        ]
    ]
)



