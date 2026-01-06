# Authored By Certified Coders © 2025
from datetime import datetime

from pyrogram import filters
from pyrogram.types import Message
from config import *
from AnnieXMedia import app
from AnnieXMedia.core.call import StreamController
from AnnieXMedia.utils import bot_sys_stats
from AnnieXMedia.utils.media_helper import send_smart_media
from AnnieXMedia.utils.decorators.language import language
from AnnieXMedia.utils.inline import supp_markup
from config import BANNED_USERS, PING_IMG_URL


@app.on_message(filters.command("ping", prefixes=["/", "."]) & ~BANNED_USERS)
@language
async def ping_com(client, message: Message, _):
    start = datetime.now()
    response = await send_smart_media(
        client=client,
        chat_id=message.chat.id,
        url_or_file=PING_IMG_URL,
        caption=_["ping_1"].format(app.mention),
        reply_to_message_id=message.id
    )
    pytgping = await StreamController.ping()
    UP, CPU, RAM, DISK = await bot_sys_stats()
    resp = (datetime.now() - start).microseconds / 1000
    await response.edit_text(
        _["ping_2"].format(resp, app.mention, UP, RAM, CPU, DISK, pytgping),
        reply_markup=supp_markup(_),
    )
