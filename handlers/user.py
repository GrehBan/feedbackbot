from loader import dp
import logging
from constants import data, users, SUPERUSER_ID
from utils import dump_data, send

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
    await msg.answer(text=data["my_projects"], parse_mode='HTML')


@dp.message_handler(text="contacts")
async def contacts(msg: Message):
    await msg.answer(text=data["contacts"], parse_mode='HTML')


@dp.message_handler(content_types=ContentType.ANY)
async def feedback_msg(msg: Message):
    await msg.answer(text="thanks for contacting, expect a response")
    if msg.content_type != 'text':
        if not msg.caption:
            msg.caption = f"#ID{msg.from_user.id}"
        else:
            msg.caption += f"\n\n#ID{msg.from_user.id}"
    else:
        msg.text += f"\n\n#ID{msg.from_user.id}"

    await send(user_id=SUPERUSER_ID, msg=msg, content_type=msg.content_type)
