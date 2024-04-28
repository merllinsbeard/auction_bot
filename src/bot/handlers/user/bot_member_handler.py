from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command

member_router = Router()

@member_router.message(F.text, Command)