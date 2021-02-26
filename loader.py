from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from constants import TOKEN
import logging


bot = Bot(token=TOKEN, parse_mode="HTML")
dp = Dispatcher(bot=bot, storage=MemoryStorage())

logging.basicConfig(handlers=[logging.StreamHandler(), ], level=logging.INFO)
logging.getLogger('aiogram').setLevel(logging.INFO)
