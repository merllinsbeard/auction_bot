from aiogram import Router
from aiogram.exceptions import TelegramAPIError
from aiogram.types import ChatMemberAdministrator
from aiogram.enums.parse_mode import ParseMode
import logging

from BotSingleton import BotSingleton
from config import BOT_TOKEN, BOT_ADMIN
from ORM.models import Channel, Auction, Member

bot = BotSingleton(BOT_TOKEN)


async def create_auction(channel_id, prize):
    channel = await Channel.get_or_none(channel_id)
    if await check_access_to_channel(channel_id) and channel:
        try:
            await Auction.create_auction(
                channel=channel,
                prize=prize,                      
            )
        except Exception as e:
            logging.exception(f'ошибка создания аукциона Auction.create_auction: {e}')
            
        await bot.send_message(
            chat_id=channel_id,
            text='вафафаф',
            parse_mode=ParseMode.MARKDOWN,
            # reply_markup=''
        )


async def check_access_to_channel(channel_id):
    try:
        chat = None
        
        try:
            chat = await bot.get_chat(channel_id)
        except TelegramAPIError as e:
            logging.error(f'ошибка при получении информации о канале: {e}')
            await bot.send_message(
                chat_id=int(BOT_ADMIN),
                text=f'Бот не добавлен в чат: ({channel_id})'
            )
            return False
            
        if chat:
            bot_info = await bot.get_me()
            bot_status = await bot.get_chat_member(channel_id, bot_info.id)
            
            if isinstance(bot_status, ChatMemberAdministrator):
                return True
            
            else:
                await bot.send_message(
                chat_id=int(BOT_ADMIN),
                text=f'Бот не является администратором этого канала: ({channel_id})'
                )
                return False
    
    except TelegramAPIError as e:
        logging.exception(f'Неизвестная ошибка в методе check_access_to_channel')
        return False