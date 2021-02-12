from loader import dp
import logging
from constants import data, users
from utils import dump_data

from aiogram.dispatcher.filters import CommandStart
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.types.message import ContentType

logger = logging.getLogger(__name__)

@dp.message_handler(CommandStart())
async def start_cmd(msg: Message):
	kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
	kb.insert(KeyboardButton(text="my projects"))
	kb.insert(KeyboardButton(text="contacts"))
	
	await msg.answer(text="Hi, i'm a feedback bot with @grehban", reply_markup=kb)
	user_id = str(msg.from_user.id)
	if user_id not in users:
		users.update({user_id: {}})
		dump_data('users.json', users)


@dp.message_handler(text="my projects")
async def my_projects(msg: Message):
	await msg.answer(text=data["my_projects"])


@dp.message_handler(text="contacts")
async def contacts(msg: Message):
	await msg.answer(text=data["contacts"])

		
@dp.message_handler(content_types=ContentType.ANY)
async def feedback_msg(msg: Message):
	await msg.answer(text="thanks for contacting, expect a response") 
	msg.caption += f"\n\n#ID{msg.from_user.id}"
	await msg.copy_to(chat_id=SUPERUSER_ID)