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

