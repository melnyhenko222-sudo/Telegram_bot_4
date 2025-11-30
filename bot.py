import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
from aiogram.utils import executor

# Токен бота, який дає BotFather
API_TOKEN = '8530525331:AAE9BvokXk9UcFBtvJRKZN0K1hWAraKY7po'

# Налаштування логування
logging.basicConfig(level=logging.INFO)

# Ініціалізація бота і диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Команда /start
@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.reply("Привіт! Я простий бот на aiogram.")

# Запуск бота
if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)
