from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext


from bot.fsm.fsm_states import AdminMenuStates
from bot.keyboards.admin_keyboard import MAIN_MENU
from config import BOT_ADMIN

admin_messages_router = Router()

@admin_messages_router.message(F.text, Command('start'))
async def start_command(message: Message, state: FSMContext):
    if message.from_user.id == int(BOT_ADMIN):
        await state.set_state(AdminMenuStates.MENU)
        await message.answer(
            text='Это бот для создания аукционов в вашем канале',
            reply_markup=MAIN_MENU
        )
    else:
        await message.answer(
            text='У вас нет доступа'
        )
