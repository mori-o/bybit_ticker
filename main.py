import asyncio
from bot import bot, dp, send_periodic_message

async def main():
    asyncio.create_task(send_periodic_message())
    print("Бот запущен и готов к работе")
    try:
        await dp.start_polling(bot)
    except KeyboardInterrupt:
        print("\nПрограмма завершена пользователем")
        await bot.close()
        exit(0)

if __name__ == "__main__":
    asyncio.run(main())