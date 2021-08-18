from environs import Env

# Теперь используем вместо библиотеки python-dotenv библиотеку environs
env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")  # Забираем значение типа str
ADMINS = env.list("ADMINS")  # Тут у нас будет список из админов
VK_TOKEN = env.str("VK_TOKEN")  # str для токена ВК-приложения
VK_AUTH_LINK = env.str("VK_AUTH_LINK")  # str ссылка на авторизацию пользователя
ip = env.str("ip")  # Тоже str, но для айпи адреса хоста
DB_PASS = env.str("DB_PASS")
DB_USER = env.str("DB_USER")



