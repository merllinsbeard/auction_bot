import yaml
import os
import logging
from aiomysql import create_pool


from .database_model import ChannelTable

current_dir = os.path.dirname(os.path.abspath(__file__))
conf = os.path.join(current_dir, "..", "..", "config.yaml")

with open(conf, "r") as conf_file:
    data = yaml.safe_load(conf_file)
    HOST = data.get("HOST")
    PORT = data.get("PORT")
    USER = data.get("USER")
    PASSWORD = data.get("PASSWORD")


async def init_db():
    try:
        pool = await create_pool(
            host=HOST,
            port=PORT,
            user=USER,
            password=PASSWORD,
            db='auction_bot',
        )
    except Exception as e:
        logging.exception(f'ошибка в функции init_db при создании пула')
    channel_table = ChannelTable(pool)
    await channel_table.init_table()
    return {
        'channel_table': channel_table
    }
    
