from aiogram import Router, F
from aiogram.filters import Command
from aiogram import types

router1 = Router()

@router1.message(F.text, Command('start'))
async def start(message: types.Message):
    await message.answer('hello')