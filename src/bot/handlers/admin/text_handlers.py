from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.filters import StateFilter
from aiogram.enums.parse_mode import ParseMode
import asyncio


from bot.fsm.fsm_states import AdminMenuStates
from bot.keyboards.admin_keyboard import MAIN_MENU, START_OR_NO
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

@admin_messages_router.message(StateFilter(AdminMenuStates.WAIT_PRIZE_INPUT), F.text)
async def write_prize_input(message: Message, state: FSMContext):
    try:
        prize = int(message.text)
        data = await state.get_data()
        channel_title = data['chosen_channel']
        
        await message.answer(
            text=f'***Канал:*** {channel_title}\n***Приз:*** {prize}',
            reply_markup=START_OR_NO,
            parse_mode=ParseMode.MARKDOWN
        )
        
    except ValueError:
        caution = await message.answer('Введите приз в правильном формате')
        await asyncio.sleep(3)
        await caution.delete()