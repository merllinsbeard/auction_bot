from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import ChatMemberUpdated
import logging
import asyncio


from bot.keyboards.admin_keyboard import MAINMENU, STARTBUTTONS, BACKTOMAINMENU
from bot.fsm.fsm_states import AdminMenuStates
from CRUD.db_connector import DatabaseConnector



callbacks_admin_router = Router()


@callbacks_admin_router.callback_query(StateFilter(AdminMenuStates.start), F.data == "mainmenu")
async def main_menu_button(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text(text="Главное меню", reply_markup=MAINMENU)
    await state.set_state(AdminMenuStates.mainmenu)
    await callback.answer()


@callbacks_admin_router.callback_query(StateFilter(AdminMenuStates.start), F.data == "statistics")
async def main_menu_button(callback: CallbackQuery, state: FSMContext):
    pass


@callbacks_admin_router.callback_query(StateFilter(AdminMenuStates.mainmenu), F.data == "backtostartbuttons")
async def backtomainmenu(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text(
        text="Это бот для создания аукционов в вашем канале", reply_markup=STARTBUTTONS
    )
    await callback.answer()
    await state.set_state(AdminMenuStates.start)


@callbacks_admin_router.callback_query(StateFilter(AdminMenuStates.mainmenu, F.data == "channels"))
async def add_channel(callback: CallbackQuery, state: FSMContext):

    await callback.message.edit_text(
        text="тут будут добавленные каналы", reply_markup=BACKTOMAINMENU
    )
    await state.set_state(AdminMenuStates.channels)


@callbacks_admin_router.my_chat_member()
async def bot_added_to_channel(update: ChatMemberUpdated, state: FSMContext):
    if update.new_chat_member.status == "administrator":
        chat_id = update.chat.id
        chat = await update.bot.get_chat(chat_id)
        title = chat.title
        user = update.from_user.id
        await update.bot.send_message(
            chat_id=user,
            text=f'Бот был добавлен как администратор в канал {title}'
        )
        try:
            db_connector = await DatabaseConnector.get_instance()
            channel_table = db_connector.channel_table
            await channel_table.add_channel(chat_id, title)
        except Exception as e:
            logging.exception(f'ошибка при использовании databaseconnector в обработчике bot_added_to_channel')


@callbacks_admin_router.callback_query(
    StateFilter(AdminMenuStates.channels), F.data == "backtomainmenu"
)
async def backtomainmenu(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text(text="Главное меню", reply_markup=MAINMENU)
    await state.set_state(AdminMenuStates.mainmenu)
    await callback.answer()
