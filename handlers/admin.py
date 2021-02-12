from loader import dp
from constants import data, SUPERUSER_ID, ID_REGEXP, users
import logging
from utils import dump_data, States

from aiogram.types.message import ContentType
from aiogram.utils.exceptions import BotBlocked, UserDeactivated
from aiogram.types import (
	Message, CallbackQuery,
	InlineKeyboardMarkup,
	InlineKeyboardButton)
	

logger = logging.getLogger(__name__)


@dp.message_handler(commands=["admin"], chat_id=SUPERUSER_ID,
state="*")
async def admin_menu(msg: Message):
	kb = InlineKeyboardMarkup(row_width=2)
	kb.insert(InlineKeyboardButton(text="statistics", callback_data="stat"))
	kb.insert(InlineKeyboardButton(text="texts", callback_data="texts"))
	kb.insert(InlineKeyboardButton(text="mailing", callback_data="mailing"))
	await msg.answer(text="admin menu", reply_markup=kb)
	
	
@dp.callback_query_handler(text="texts", chat_id=SUPERUSER_ID)
async def texts_menu(c: CallbackQuery):
    await c.answer()
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton(text="my projects text", 
callback_data="edit_text:my_projects"))
    kb.add(InlineKeyboardButton(text="contacts text", 
callback_data="edit_text:contacts"))
    kb.add(InlineKeyboardButton(text="back", callback_data="back"))
    
    await c.message.edit_reply_markup(reply_markup=kb)


@dp.callback_query_handler(text="edit_text:my_projects",
chat_id=SUPERUSER_ID)
async def edit_text_my_projects(c: CallbackQuery):
    await c.answer()
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton(text="back", callback_data="back"))
    
    await c.message.edit_text(text="send new text for my projects tab", reply_markup=kb)
    await States.my_projects.set()

    
@dp.callback_query_handler(text="edit_text:contacts", 
chat_id=SUPERUSER_ID)
async def edit_text_contacts(c: CallbackQuery):
    await c.answer()
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton(text="back", callback_data="back"))
    
    await c.message.edit_text(text="send new text for contacts tab", reply_markup=kb)
    await States.contacts.set()
   

@dp.callback_query_handler(chat_id=SUPERUSER_ID, state="*")
async def stat(c: CallbackQuery):
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton(text="back", callback_data="back"))
    await c.message.edit_text(text=f"users in bot: {len(users)}", reply_markup=kb)
    
    
@dp.message_handler( chat_id=SUPERUSER_ID, state=States.my_projects)
async def save_my_projects(msg: Message, state):
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton(text="back", callback_data="back"))
    await msg.answer(text="text saved", reply_markup=kb)
    data["my_projects"]=msg.html_text
    dump_data("data.json", data)
    await state.finish()
 

@dp.message_handler( chat_id=SUPERUSER_ID, state=States.contacts)
async def save_contacts(msg: Message, state):
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton(text="back", 
callback_data="back"))
    await msg.answer(text="text saved", reply_markup=kb)
    data["contacts"]=msg.html_text
    dump_data("data.json", data)
    await state.finish()
    
    
    
@dp.message_handler(is_reply=True, chat_id=SUPERUSER_ID,
content_types=ContentType.ANY)
async def new_message(msg: Message):
	
	user_id = ID_REGEXP.search(msg.text)
	if not user_id:
		return
	user_id = int(user_id.group(1))
	try:
		await msg.copy_to(chat_id=user_id)
	except BotBlocked:
		await msg.answer(text="the user has blocked the bot")
	except UserDeactivated:
		await msg.answer(text="user deactivated")
	except Exception as exc:
		logger.error("unknown error %s" % exc)
		
