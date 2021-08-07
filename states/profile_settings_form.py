from aiogram.dispatcher.filters.state import StatesGroup, State


class Profile_settings(StatesGroup):
    age = State()
    location = State()
    earning = State()
