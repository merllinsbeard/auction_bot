from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
import logging
from aiogram.enums.parse_mode import ParseMode



from bot.keyboards.admin_keyboard import MAIN_MENU, ADDED_CHANNELS_BACK, START_OVER, generate_channel_keyboard
from bot.fsm.fsm_states import AdminMenuStates
from ORM.models import Channel
from config import BOT_ADMIN

callbacks_admin_router = Router()

@callbacks_admin_router.callback_query(StateFilter(AdminMenuStates.MENU), F.data == 'START_AUCTION')
async def start_auction_button(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text('***Выберите канал***', reply_markup=await generate_channel_keyboard(), parse_mode=ParseMode.MARKDOWN)
    await state.set_state(AdminMenuStates.ADDED_CHANNELS)
    await callback.answer()


@callbacks_admin_router.callback_query(StateFilter(AdminMenuStates.ADDED_CHANNELS), F.data.startswith('page_'))
async def page_navigation(callback: CallbackQuery):
    _, page_number = callback.data.split('_')
    page = int(page_number)
    
    new_keyboard = await generate_channel_keyboard(page=page)
    
    await callback.message.edit_text(
        '***Выберите канал***',
        reply_markup=new_keyboard,
        parse_mode=ParseMode.MARKDOWN
    )
    await callback.answer()
    

@callbacks_admin_router.callback_query(StateFilter(AdminMenuStates.ADDED_CHANNELS), F.data.startswith('channel_'))
async def start_auction_setup(callback: CallbackQuery, state: FSMContext):
    await state.set_state(AdminMenuStates.CHANNEL_IS_CHOISEN)
    _, channel_id = callback.data.split('_')
    channel_title = await Channel.get_channel_title(channel_id)
    
    await callback.message.edit_text(
        text=f'***Канал:*** {channel_title}\n\nВведите приз аукциона',
        reply_markup=START_OVER,
        parse_mode=ParseMode.MARKDOWN
    )
    
    await state.update_data(chosen_channel=channel_title)
    await state.set_state(AdminMenuStates.WAIT_PRIZE_INPUT)
    
    
@callbacks_admin_router.callback_query(StateFilter(AdminMenuStates.WAIT_PRIZE_INPUT), F.data == 'start_over')
async def start_over(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text('***Выберите канал***', reply_markup=await generate_channel_keyboard(), parse_mode=ParseMode.MARKDOWN)
    await state.set_state(AdminMenuStates.ADDED_CHANNELS)
    await callback.answer()
    
    
@callbacks_admin_router.callback_query(StateFilter(AdminMenuStates.ADDED_CHANNELS), F.data == 'go_to_main_menu_from_added_channels')
async def back_to_main_from_added_channels(callback: CallbackQuery, state: FSMContext):
    await state.set_state(AdminMenuStates.MENU)
    await callback.message.edit_text(
            text='Это бот для создания аукционов в вашем канале',
            reply_markup=MAIN_MENU
        )
    await callback.answer()
    

@callbacks_admin_router.callback_query(StateFilter(AdminMenuStates.MENU), F.data == 'ADDED_CHANNELS')
async def show_added_channels_button(callback: CallbackQuery, state: FSMContext):
    channels_text = await Channel.get_channels_list_format()
    await callback.message.edit_text(
        text=channels_text,
        reply_markup=ADDED_CHANNELS_BACK,
        parse_mode=ParseMode.HTML
    )
    await state.set_state(AdminMenuStates.ADDED_CHANNELS)
    await callback.answer()


@callbacks_admin_router.callback_query(StateFilter(AdminMenuStates.ADDED_CHANNELS), F.data == 'back_to_main_from_added_channels')
async def back_to_main(callback: CallbackQuery, state: FSMContext):
    if callback.from_user.id == int(BOT_ADMIN):
        await state.set_state(AdminMenuStates.MENU)
        await callback.message.edit_text(
            text='Это бот для создания аукционов в вашем канале',
            reply_markup=MAIN_MENU
        )
    else:
        await callback.message.answer(
            text='У вас нет доступа'
        )
    await callback.answer()


@callbacks_admin_router.callback_query(StateFilter(AdminMenuStates.MENU), F.data == 'STATISTICS')
async def show_statistics_button(callback: CallbackQuery, state: FSMContext):
    
    await callback.answer()

