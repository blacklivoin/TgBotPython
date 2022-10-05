import asyncio

from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.markdown import text

TOKEN = '5333399315:AAFm_-enErHml7qD84Ag4J2j5Fnwm1YrDAY'
bot = Bot(TOKEN, parse_mode="HTML")
dp = Dispatcher(bot)


if __name__ == '__main__':
    from handlers import *
    executor.start_polling(dp, skip_updates=True)
