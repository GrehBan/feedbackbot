from aiogram.types import Message
from aiogram import Bot


async def send(content_type: str, user_id: int, msg: Message,
               disable_web_page_preview: bool = False,
               disable_notification: bool = False):

    bot = Bot.get_current()
    if content_type == 'text':
        ms = await bot.send_message(chat_id=user_id, text=msg.text, parse_mode=msg.bot.parse_mode,
                                    reply_markup=msg.reply_markup,
                                    disable_web_page_preview=disable_web_page_preview,
                                    disable_notification=disable_notification)
    else:
        if content_type == 'video':
            ms = await bot.send_video(chat_id=user_id, video=msg.video.file_id,
                                      reply_markup=msg.reply_markup,
                                      parse_mode=msg.bot.parse_mode,
                                      caption=msg.caption)

        elif content_type == 'photo':
            ms = await bot.send_photo(chat_id=user_id, photo=msg.photo[-1].file_id, reply_markup=msg.reply_markup,
                                      parse_mode=msg.bot.parse_mode, caption=msg.caption)
        elif content_type == 'animation':
            ms = await bot.send_animation(chat_id=user_id, animation=msg.animation.file_id,
                                          reply_markup=msg.reply_markup,
                                          parse_mode=msg.bot.parse_mode, caption=msg.caption)
        elif content_type == 'audio':
            ms = await bot.send_audio(chat_id=user_id, audio=msg.audio.file_id, caption=msg.caption,
                                      reply_markup=msg.reply_markup, parse_mode=msg.bot.parse_mode)
        elif content_type == 'document':
            ms = await bot.send_document(chat_id=user_id, document=msg.document.file_id, caption=msg.caption,
                                         reply_markup=msg.reply_markup, parse_mode=msg.bot.parse_mode)
        elif content_type == 'sticker':
            ms = await bot.send_sticker(chat_id=user_id, sticker=msg.sticker.file_id, reply_markup=msg.reply_markup)
        else:
            return
    return ms
