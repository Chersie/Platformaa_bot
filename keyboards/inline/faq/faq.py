from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.faq.callback_datas import read_faq_callback_data, vk_register_callback_data

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

vk_registration_menu_without_faq_readed_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🔹 Привязать ВКонтакте", callback_data=vk_register_callback_data.new(want_to_register="Yes")),
            InlineKeyboardButton(text="⌚ Я ленивый, привяжу потом", callback_data=vk_register_callback_data.new(want_to_register="No")),
        ],
        [
            InlineKeyboardButton(text="📖 Я передумал, хочу прочитать FAQ", callback_data=read_faq_callback_data.new(want_to_read="Yes")),
        ]
    ]
)

vk_registration_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🔹 Привязать ВКонтакте",
                                 callback_data=vk_register_callback_data.new(want_to_register="Yes")),
            InlineKeyboardButton(text="⌚ Привяжу потом",
                                 callback_data=vk_register_callback_data.new(want_to_register="No")),
        ]
    ]
)