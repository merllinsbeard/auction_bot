from aiogram import Bot

class BotSingleton:
    _instance = None
    
    def __new__(cls, TOKEN):
        if cls._instance is None:
            cls._instance = Bot(token=TOKEN)
        return cls._instance
    
