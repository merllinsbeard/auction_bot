from aiogram import Router, F
from aiogram.filters import Command, StateFilter
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
import logging


from bot.fsm.fsm_states import AdminMenuStates
from bot.keyboards.admin_keyboard import STARTBUTTONS, MAINMENU

admin_messages_router = Router()

@admin_messages_router.message(F.text, Command('start'))
async def start_cmd(message: Message, state: FSMContext):
    await message.answer(
        text='Это бот для создания аукционов в вашем канале',
        reply_markup=STARTBUTTONS
    )
    await state.set_state(AdminMenuStates.start)
    

# @admin_messages_router.message(F.text, StateFilter(AdminMenuStates.add_channel))
# async def add_channel(message: Message, state: FSMContext):
#     ...