from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
import os, asyncio, logging

from handlers.routers import router1


logging.basicConfig(filename='bot.log',
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s'
                    )

load_dotenv()
TOKEN = os.getenv('TOKEN')

bot = Bot(TOKEN)
dp = Dispatcher()


async def main():

    dp.include_routers(router1)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())