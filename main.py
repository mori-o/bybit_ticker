import asyncio
from aiogram.types import BotCommand
from bot import bot, dp, send_periodic_message

async def setup_bot_commands():
    bot_commands = [
        BotCommand(command="/start", description="to check current crypto rates instantly")
    ]
    await bot.set_my_commands(bot_commands)

async def main():
    try:
        await setup_bot_commands()
        asyncio.create_task(send_periodic_message())
        print("Бот запущен и готов к работе")
        await dp.start_polling(bot, skip_updates=True)
    except KeyboardInterrupt:
        print("\nПрограмма завершена пользователем")
        await bot.close()
        exit(0)

if __name__ == "__main__":
    asyncio.run(main())