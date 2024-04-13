from aiocryptopay import AioCryptoPay, Networks
from aiocryptopay.models.update import Update
import asyncio
from aiohttp import web


# from . import TOKEN_CRYPTO


# # web = web.Application()
# crypto = AioCryptoPay('12348:AAAXtE4Q4mmzixH33DxHkMEhmWbfJd8hczr', network=Networks.TEST_NET)

# DESCRIPTION = "Оплатите участие"

# async def create_invoice(amount: int):
#     invoice = await crypto.create_invoice(currency_type='fiat', fiat='RUB', amount=amount, description=DESCRIPTION, payload='user_id')
#     print(invoice.expiration_date)
#     int


