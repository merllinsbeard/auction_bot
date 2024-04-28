from aiogram import Dispatcher
import asyncio
import logging

from BotSingleton import BotSingleton
from bot.handlers.admin.text_handlers import admin_messages_router
from bot.handlers.admin.button_handlers import callbacks_admin_router
from bot.handlers.channel.added_tochannel_router import router_addbot_tochannel
from ORM.init_db import DatabaseConnector
from config import BOT_TOKEN


logging.basicConfig(filename='bot.log',
                    level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s'
                    )


bot = BotSingleton(BOT_TOKEN)
dp = Dispatcher()


async def main():
    
    try:
        await DatabaseConnector.get_instance()
    except Exception as e:
        logging.exception(f'ошибка подключения DatabaseConnector.get_instance(): {e}')
        
    dp.include_routers(
        admin_messages_router,
        callbacks_admin_router,
        router_addbot_tochannel
    )
    
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
