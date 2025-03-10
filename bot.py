import asyncio
from api import get_prices
from aiogram.types import Message
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from config import TOKEN, CHAT_ID, ALLOWED_IDS, THREAD_ID

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    user_id = message.from_user.id
    if user_id is not None and user_id in ALLOWED_IDS:
        prices = get_prices()
        await message.answer(prices, parse_mode="Markdown")
        print(f"Информация отправлена пользователю {user_id}")
    else:
        await message.answer(f"У вашего ID ({user_id}) нет доступа к боту, обратитесь к @morio_ohh для получения доступа.")
        
async def send_periodic_message():
    while True:
        prices = get_prices()
        await bot.send_message(chat_id=CHAT_ID, text=prices, parse_mode="Markdown", message_thread_id=THREAD_ID)
        print(f"Периодическое сообщение отправлено в группу {CHAT_ID}, тред {THREAD_ID}")

        await asyncio.sleep(3600)