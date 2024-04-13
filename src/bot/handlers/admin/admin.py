from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message
import logging


from bot.keyboards.admin_keyboard import STARTBUTTONS, MAINMENU


admin_messages_router = Router()

@admin_messages_router.message(F.text, Command('start'))
async def start_cmd(message: Message):
    await message.answer(
        text='Это бот для создания аукционов в вашем канале',
        reply_markup=STARTBUTTONS
    )
    
