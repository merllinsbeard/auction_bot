from tortoise.models import Model
from tortoise import fields
import uuid
import logging
from datetime import datetime 


class Channel(Model):
    channel_id = fields.BigIntField(pk=True)
    channel_name = fields.CharField(max_length=255)
    auctions = fields.ReverseRelation["Auction"]
    
    class Meta:
        table = "channels"

    @classmethod
    async def add_or_update_channel(cls, channel_id, channel_name):
        try:
            channel = await cls.get_or_none(channel_id=channel_id)
            if channel:
                channel.channel_name = channel_name
                await channel.save()
                logging.info(f'Канал с ID {channel_id} обновлен: новое название - {channel_name}')
            else:
                await cls.create(channel_id=channel_id, channel_name=channel_name)
                logging.info(f'Канал с ID {channel_id} добавлен с названием {channel_name}')
        except Exception as e:
            logging.error(f'ошибка при добавлении или обновлении канала {channel_id}: {e}')
            raise
            
    @classmethod
    async def remove_channel(cls, channel_id):
        try:
            await cls.filter(channel_id=channel_id).delete()
        except Exception as e:
            logging.error(f'Ошибка при удалении канала {channel_id}: {e}')
            raise 
        
    @classmethod
    async def get_channels_list_format(cls):
        try:
            channels = await cls.all().values('channel_id', 'channel_name')
            if channels:
                lines = []
                for channel in channels:
                    auctions_count = await cls.count_auctions(channel['channel_id'])
                    lines.append(
                        f"💎 {channel['channel_name']}\n     🔗Id: {channel['channel_id']}\n     🔗Кол-во аукционов: {auctions_count}"
                    )
                return "<b>Добавленные каналы:</b>\n\n" + "\n".join(lines)
            else:
                return "У вас нет подключенных каналов."
        except Exception as e:
            logging.error(f'Ошибка в методе get_channels_list_format: {e}')
            return "Ошибка при загрузке списка каналов"
        
    @classmethod
    async def count_auctions(cls, channel_id):
        count = await Auction.filter(channel_id=channel_id).count()
        return count

    @classmethod
    async def get_channel_title(cls, channel_id):
        channel = await cls.get_or_none(channel_id=channel_id)
        if channel:
            return channel.channel_name
        else:
            return None
        
            
    
class Auction(Model):
    id = fields.CharField(pk=True, max_length=50)
    channel = fields.ForeignKeyField('models.Channel', related_name='auctions')  # связь с моделью Channel
    number_of_members = fields.IntField(default=0)
    time_of_start = fields.DatetimeField()
    time_of_end = fields.DatetimeField(null=True)
    last_bet_time = fields.DatetimeField(null=True)
    auction_bank = fields.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    prize = fields.IntField()
    
    class Meta:
        table = "auctions"
    
    @classmethod
    async def create_auction(cls, channel: Channel, prize):
        id = cls.generate_unique_id()
        auction = await cls.create(
            id=id,
            channel=channel,
            time_of_start=cls.get_now_time(),
            prize=prize
        )
        return auction
        
    @staticmethod
    def generate_unique_id():
        return str(uuid.uuid4())
    
    @staticmethod
    def get_now_time():
        return datetime.now()
    
    @classmethod
    async def write_end_time(cls, auction_id, end_time):
        auction = await cls.get(id=auction_id)
        auction.time_of_end = end_time
        await auction.save()
    
    @classmethod
    async def write_last_bet_time(cls, auction_id, last_bet_time):
        auction = await cls.get(id=auction_id)
        auction.last_bet_time = last_bet_time
        await auction.save()
    
    @classmethod
    async def plus_one_member():
        pass


class Member(Model):
    ...