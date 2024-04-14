import aiomysql
import logging
from aiomysql import Pool, create_pool

class DatabaseModel:
    def __init__(self, pool: Pool):
        self.pool = pool
        logging.info('создан пул в базовом классе DatabaseModel')

    async def execute(self, query, args=None):
        try:
            async with self.pool.acquire() as conn:
                async with conn.cursor() as cursor:
                    await cursor.execute(query, args)
                    await conn.commit()
                    return cursor
        except Exception as e:
            logging.exception(f'ошибка в методе execute базового класса DatabaseModel {e}')


    async def fetch(self, query, args=None):
        try:
            async with self.pool.acquire() as conn:
                async with conn.cursor(aiomysql.DictCursor) as cursor:
                    await cursor.execute(query, args)
                    result = await cursor.fetchall()
                    return result
        except Exception as e:
            logging.exception(f'ошибка в методе fetch базового класса DatabaseModel {e}')


class ChannelTable(DatabaseModel):

    async def init_table(self):
        create_table_query = """
        CREATE TABLE IF NOT EXISTS Channels (
            channel_id BIGINT PRIMARY KEY,
            channel_name VARCHAR(255),
            auction_sum INT 
        );
        """
        try:
            await self.execute(create_table_query)
            logging.info(f'создана успешно таблица для каналов')
        except Exception as e:
            logging.exception(f"Ошибка в методе init_table класса ChannelTable: {e}")

    async def add_channel(self, channel_id, channel_name):
        query = """
        INSERT INTO Channels (channel_id, channel_name, auction_sum) VALUES (%s, %s, %s);
        """
        try:
            await self.execute(query, (channel_id, channel_name, 0))
            logging.info(f'успешно добавлен канал через метод add_channel класса ChannelTable ')
        except Exception as e:
            logging.exception(f"Ошибка в методе add_channel класса ChannelTable: {e}")


    async def get_channels(self):
        try:
            query = "SELECT * FROM Channels"
            res = await self.fetch(query)
            logging.info(f'успешно выведена информация с помощью get_channels класса ChannelTable')
        except Exception as e:
            logging.exception(f"ошибка в методе get_channels класса ChannelTable: {e}")

        return res


# class AuctionsTable(DatabaseModel):
#     async def add_post(self, channel_id, content, timestamp):
#         query = "INSERT INTO Posts (channel_id, content, timestamp) VALUES (%s, %s, %s)"
#         await self.execute(query, (channel_id, content, timestamp))

#     async def get_posts_by_channel(self, channel_id):
#         query = "SELECT * FROM Posts WHERE channel_id = %s"
#         return await self.fetch(query, (channel_id,))


# class AuctionUsers(DatabaseModel):
#     async def add_subscriber(self, channel_id, user_id, subscribe_date):
#         query = "INSERT INTO Subscribers (channel_id, user_id, subscribe_date) VALUES (%s, %s, %s)"
#         await self.execute(query
