import asyncio
from api import get_prices
from aiogram import Bot, Dispatcher
from aiogram.types import Message, BotCommand
from aiogram.filters import CommandStart
from config import TOKEN, CHAT_ID, THREAD_ID

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    user_id = message.from_user.id
    prices = get_prices()
    await message.answer(prices, parse_mode="Markdown")
    print(f"Информация отправлена пользователю {user_id}")
        
async def send_periodic_message():
    while True:
        prices = get_prices()
        await bot.send_message(chat_id=CHAT_ID, text=prices, parse_mode="Markdown", message_thread_id=THREAD_ID)
        print(f"Периодическое сообщение отправлено в группу {CHAT_ID}, тред {THREAD_ID}")
        await asyncio.sleep(3600)