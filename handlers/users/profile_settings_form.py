from aiogram.types import Message, Location, ReplyKeyboardRemove
from aiogram.dispatcher.filters import Command
from aiogram.utils.callback_data import CallbackData

from telegram import CallbackQuery

from keyboards.inline.profile_settings.callback_datas import age_callback_data
from keyboards.inline.profile_settings.profile_settings import select_age_keyboard, get_location_keyboard, \
    has_earning_keyboard
from loader import dp


@dp.callback_query_handler(text="settings")
async def form_age(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_text(text="Выберите свой возраст:",
                                 reply_markup=select_age_keyboard)

@dp.callback_query_handler(age_callback_data.filter())
async def form_location(call: CallbackQuery, callback_data: dict):
    print(callback_data["age"]) # обрабатываем и записываем в БД возраст
    await call.answer(cache_time=60)
    await call.message.edit_text(text="А на аватарке выглядите намного моложе!", reply_markup=None)
    await call.message.answer(text="Выберите город в котором проживаете:\n"
                                      "P.S. Данная информация нужна исключительно для подбора"
                                      "персонализированных заданий, за котоые вы сможете"
                                      "получать больше денег, чем за обычные\n"
                                      "P.P.S. Данные параметры ты сможешь всегда изменить в"
                                      "личном профиле",
                                 reply_markup=get_location_keyboard)


@dp.message_handler(content_types=["location"])
async def form_earning(message: Message):
    location = message.location
    print(location.latitude, location.longitude) # обрабатываем и записываем геолокацию в БД
    await message.answer(text="Отлично! И последний вопрос.\n"
                              "Имеешь ли ты личный источник дохода? (работа, личное дело и тд.)",
                         reply_markup=ReplyKeyboardRemove,
                         reply_markup=has_earning_keyboard)