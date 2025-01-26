import asyncio
import logging
import sys

from config import bot, dp
from src.routers.handlers2 import router2


async def start():
    dp.include_router(router2)
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(start())