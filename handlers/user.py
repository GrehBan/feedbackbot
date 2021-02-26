from loader import dp
import logging
from constants import data, users, SUPERUSER_ID
from utils import send
from utils.db import get_sql, set_sql

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

    user_id = msg.from_user.id
    exists = await get_sql("SELECT user_id FROM users WHERE user_id=?", user_id)
    if not exists:
        await set_sql("INSERT INTO users(user_id) VALUES(?)", user_id)



@dp.message_handler(text="my projects")
async def my_projects(msg: Message):
    text = await get_sql('SELECT projects FROM texts')[0]
    await msg.answer(text=text, parse_mode='HTML')


@dp.message_handler(text="contacts")
async def contacts(msg: Message):
    text = await get_sql('SELECT contacts FROM texts')[0]
    await msg.answer(text=text, parse_mode='HTML')


@dp.message_handler(content_types=ContentType.ANY)
async def feedback_msg(msg: Message):
    await msg.answer(text="thanks for contacting, expect a response")
    if msg.content_type != 'text':
        if not msg.caption:
            msg.caption = f"<a href=\"tg://user?id={msg.from_user.id}\">{msg.from_user.first_name}</a> #ID{msg.from_user.id}"
        else:
            msg.caption += f"\n\n <a href=\"tg://user?id={msg.from_user.id}\">{msg.from_user.first_name}</a> #ID{msg.from_user.id}"
    else:
        msg.text += f"\n\n<a href=\"tg://user?id={msg.from_user.id}\">{msg.from_user.first_name}</a> #ID{msg.from_user.id}"


    await send(user_id=SUPERUSER_ID, msg=msg, content_type=msg.content_type)
