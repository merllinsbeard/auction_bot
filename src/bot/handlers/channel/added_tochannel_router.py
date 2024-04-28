from aiogram import F, Router
from aiogram.filters.chat_member_updated import ChatMemberUpdatedFilter, IS_NOT_MEMBER, MEMBER, ADMINISTRATOR
from aiogram.types import ChatMemberUpdated
from aiogram.exceptions import TelegramForbiddenError
import logging
import asyncio

from ORM.models import Channel


router_addbot_tochannel = Router()


@router_addbot_tochannel.my_chat_member(ChatMemberUpdatedFilter(member_status_changed=IS_NOT_MEMBER >> ADMINISTRATOR))
async def add_bot_to_channel(event: ChatMemberUpdated):
    chat_id = event.chat.id
    await asyncio.sleep(5)
    try:
        chat = await event.bot.get_chat(chat_id)
        title = chat.title
        try:
            await Channel.add_or_update_channel(chat_id, title)
        except Exception as e:
            logging.error(f'ошибка при добавлении или обновлении канала в обработчике add_bot_to_channel{e}')
            
        logging.info(f'успешное добавление бота как администратора в канал {title} с id {chat_id} и в базу данных')
    except TelegramForbiddenError as e:
        logging.error(f'ошибка добавления {chat_id}: {e}')
        
   
        

@router_addbot_tochannel.my_chat_member(ChatMemberUpdatedFilter(member_status_changed=ADMINISTRATOR >> IS_NOT_MEMBER))
async def delete_admin_bot(event: ChatMemberUpdated):
    chat_id = event.chat.id
    try:
        try:
            await Channel.remove_channel(chat_id)
        except Exception as e:
            logging.error(f'ошибка при удалении канала в обработчике delete_admin_bot {chat_id}: {e}')
        logging.info(f'успешное удаление бота из канала с id {chat_id} и из базы данных')
        
    except TelegramForbiddenError:
        logging.error(f'ошибка удаления {chat_id}')
        

@router_addbot_tochannel.my_chat_member(ChatMemberUpdatedFilter(member_status_changed=MEMBER >> IS_NOT_MEMBER))
async def delete_member_bot(event: ChatMemberUpdated):
    chat_id = event.chat.id
    try:
        await Channel.remove_channel(chat_id)
        logging.info(f'успешное удаление бота из канала с id {chat_id} и из базы данных')
        
    except TelegramForbiddenError:
        logging.error(f'ошибка удаления {chat_id}')
        