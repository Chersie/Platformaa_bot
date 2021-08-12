from telegram import CallbackQuery

from keyboards.inline.faq.callback_datas import read_faq_callback_data
from keyboards.inline.faq.keyboards import faq_continue_keyboard
from keyboards.inline.vk_registration.keyboards import vk_registration_menu_without_faq_readed_keyboard, \
    vk_registration_menu
from loader import dp


@dp.callback_query_handler(read_faq_callback_data.filter(want_to_read="Yes"))
async def show_faq(query: CallbackQuery, callback_data: dict):
    await query.answer(cache_time=60)
    await query.message.edit_text(text="|Тут находится Фак для новичков|\n"
                                       "Очень-очень много умных мыслей.\n"
                                       "Прямо невероятно много.\n"
                                       "Ого, я поумнел.\n",
                                  reply_markup=faq_continue_keyboard)


@dp.callback_query_handler(read_faq_callback_data.filter(want_to_read="No"))
async def show_faq_vk_registration_menu(query: CallbackQuery, callback_data: dict):
    await query.answer(cache_time=60)
    await query.message.edit_text(text="Молодец, я тоже не люблю излишнюю бюрократию"
                                       "Но пара советов не помешает."
                                       "Пока ты авторизован только через Telegram, "
                                       "следовательно можешь выполнять исключительно Telegram-задания. "
                                       "Для открытия всех функций рекомендую сразу привязать аккаунт ВКонтакте.",
                                  reply_markup=vk_registration_menu_without_faq_readed_keyboard)


@dp.callback_query_handler(text="faq_readed")
async def show_vk_registration_menu(query: CallbackQuery):
    await query.answer(cache_time=60)
    await query.message.edit_text(text="Молодец! Я горжусь тобой.\n"
                                       "По статистике: 8 из 10 пользователей пропускают FAQ во время регистрации =)\n"
                                       "Сейчас время привязать аккаунт ВКонтакте и начинать платформить)",
                                  reply_markup=vk_registration_menu)
