import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import Command  # Фильтр для команд
from aiogram.types import Message

bot = Bot(token="8046033764:AAHuXtAhxP4X4eZ-AcseqLIIDnEAD4jKlAg")
dp = Dispatcher()

@dp.message(Command("start"))  # Обработчик команды /start
async def cmd_start(message: Message):
    await message.answer(
        "Добро пожаловать в бот для составления заявок на услуги грузоперевозки! "
        "Используйте команды /new для создания новой заявки, /help для получения помощи "
        "и /calc для расчета стоимости перевозки."
    )

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())