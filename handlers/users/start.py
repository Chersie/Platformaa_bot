from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp

from keyboards.default.start.start_menu_keyboard import start_menu_keyboard
from keyboards.inline.profile_settings.keyboards import change_personal_info_keyboard


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(text="Ты успешно присоединился к нам!\n"
                              "Добро пожаловать в семью Platforma.\n")
    await message.answer(text="Для улучшения персонализации и для создания более эффективных заданий, "
                              "тебе нужно указать несколько вещей.",
                         reply_markup=change_personal_info_keyboard)

