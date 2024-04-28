from aiocryptopay import AioCryptoPay, Networks
from aiocryptopay.models.update import Update
import asyncio
from aiohttp import web


class CryptoPay(AioCryptoPay):
    def __init__(self, TOKEN: str, network=Networks.TEST_NET):
        super().__init__(TOKEN, network)
    
    
    async def create_auction_invoice(self):
        await self.create_invoice()


# web = web.Application()
crypto = AioCryptoPay('', network=Networks.TEST_NET)

DESCRIPTION = "Оплатите участие"

async def create_invoice(amount: int):
    invoice = await crypto.create_invoice(currency_type='fiat', fiat='RUB', amount=amount, description=DESCRIPTION, payload='user_id')
    print(invoice.expiration_date)
    int


