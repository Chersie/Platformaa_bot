from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_menu_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="FAQ"),
            KeyboardButton(text="Настройки")
        ],
        [
            KeyboardButton(text="Исполнитель"),
            KeyboardButton(text="Заказчик"),
        ]
    ]
)