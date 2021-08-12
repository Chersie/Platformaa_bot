from aiogram.dispatcher import FSMContext
from aiogram.types import Message, Location, ReplyKeyboardRemove
from aiogram.dispatcher.filters import Command
from aiogram.utils.callback_data import CallbackData

from telegram import CallbackQuery

from keyboards.default.start.start_menu_keyboard import start_menu_keyboard
from keyboards.inline.faq.keyboards import faq_start_keyboard
from keyboards.inline.profile_settings.callback_datas import age_callback_data, earning_callback_data
from keyboards.inline.profile_settings.keyboards import select_age_keyboard, get_location_keyboard, \
    has_earning_keyboard
from loader import dp

from states.profile_settings_form import Profile_settings


@dp.callback_query_handler(text="settings", state=None)
async def form_age(query: CallbackQuery, state: FSMContext):
    await query.answer(cache_time=60)
    await query.message.edit_text(text="Выберите свой возраст:",
                                 reply_markup=select_age_keyboard)
    await Profile_settings.first()


@dp.callback_query_handler(age_callback_data.filter(), state=Profile_settings.age)
async def form_location(query: CallbackQuery, callback_data: dict, state: FSMContext):
    print(callback_data["age"])  # обрабатываем и записываем в БД возраст
    await query.answer(cache_time=60)
    await query.message.edit_text(text="А на аватарке выглядите намного моложе!", reply_markup=None)
    await query.message.answer(text="Выберите город в котором проживаете:\n"
                                   "P.S. Данная информация нужна исключительно для подбора"
                                   "персонализированных заданий, за котоые вы сможете"
                                   "получать больше денег, чем за обычные\n"
                                   "P.P.S. Данные параметры ты сможешь всегда изменить в"
                                   "личном профиле",
                              reply_markup=get_location_keyboard)
    await Profile_settings.next()


@dp.message_handler(content_types=["location"], state=Profile_settings.location)
async def form_earning(message: Message, state: FSMContext):
    location = message.location
    print(location.latitude, location.longitude)  # обрабатываем и записываем геолокацию в БД
    await message.answer(text="Отлично! И последний вопрос.\n"
                              "Имеешь ли ты личный источник дохода? (работа, личное дело и тд.)",
                         reply_markup=has_earning_keyboard)
    await Profile_settings.next()


@dp.callback_query_handler(earning_callback_data.filter(), state=Profile_settings.earning)
async def form_finish(query: CallbackQuery, callback_data: dict, state: FSMContext):
    print(callback_data["has_earning"])  # обрабатываем значение и записываем в БД
    await query.answer(cache_time=60)
    await query.message.edit_text(text="Ты успешно присоединился к нам!\n"
                                      "Добро пожаловать в семью Platforma.\n",
                                 reply_markup=None)
    await query.message.answer(text="Для начала, мы рекомендуем тебе почитать FAQ для "
                                   "лучшего понимания всех наших процессов и нюансов. "
                                   "Не беспокойся, он читается быстро и легко)",
                              reply_markup=faq_start_keyboard)
    await state.finish()
