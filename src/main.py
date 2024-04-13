from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
import os
import asyncio
import logging


from bot.handlers.admin.admin import admin_messages_router


logging.basicConfig(filename='bot.log',
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s'
                    )

load_dotenv()
TOKEN = os.getenv('TOKEN')


bot = Bot(TOKEN)
dp = Dispatcher()


async def main():

    dp.include_routers(
        admin_messages_router,
    )
    
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
