from tortoise import Tortoise

from config import HOST, PORT, USER, PASSWORD

 
class DatabaseConnector:
    _instance = None

    @classmethod
    async def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
            await cls._initialize()
        return cls._instance

    @staticmethod
    async def _initialize():
        await Tortoise.init(
            db_url = f"mysql://{USER}:{PASSWORD}@{HOST}:{PORT}/auction_bot",
            modules = {"models": ["ORM.models"]}
        )
        await Tortoise.generate_schemas()





# import asyncio
# import logging

# class DatabaseConnector:
#     _instance = None
#     _channel_table = None

#     @classmethod
#     async def get_instance(cls):
#         if cls._instance is None:
#             cls._instance = cls()
#             await cls._instance._initialize()
#         logging.info('успешно использован метод get_instance')
#         return cls._instance

#     async def _initialize(self):
#         from . import init_db  
#         db_objects = await init_db()
#         self._channel_table = db_objects['channel_table']


#     @property
#     def channel_table(self):
#         return self._channel_table
