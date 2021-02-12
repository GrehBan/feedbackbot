from aiogram import Bot, Dispatcher
from aiogram.contrib.middlewares.logging import LoggingMiddleware

from constants import TOKEN
import logging

bot = Bot(token=TOKEN, parse_mode="HTML")
dp = Dispatcher(bot=bot)

dp.middleware.setup(LoggingMiddleware())