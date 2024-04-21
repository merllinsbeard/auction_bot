from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
import os
import asyncio
import logging


from bot.handlers.admin.text_handlers import admin_messages_router
from bot.handlers.admin.button_handlers import callbacks_admin_router
from ORM.init_db import DatabaseConnector


logging.basicConfig(filename='bot.log',
                    level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s'
                    )

load_dotenv()
TOKEN = os.getenv('TOKEN')


bot = Bot(TOKEN)
dp = Dispatcher()


async def main():
    
    try:
        await DatabaseConnector.get_instance()
    except Exception as e:
        logging.exception(f'ошибка подключения DatabaseConnector.get_instance(): {e}')
        
    dp.include_routers(
        admin_messages_router,
        callbacks_admin_router,
    )
    
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
