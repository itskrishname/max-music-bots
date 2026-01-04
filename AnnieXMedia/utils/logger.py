# Authored By Certified Coders © 2025
from pyrogram.enums import ParseMode

from AnnieXMedia import app
from AnnieXMedia.utils.database import is_on_off
from config import LOGGER_ID


async def play_logs(message, streamtype, query: str = None, user=None):
    if await is_on_off(2):
        if query is None:
            try:
                query = message.text.split(None, 1)[1]
            except Exception:
                query = "—"

        # Determine user and chat info
        chat_id = message.chat.id
        chat_title = message.chat.title
        chat_username = message.chat.username

        if user:
            user_id = user.id
            user_mention = user.mention
            user_username = user.username
        else:
            user_id = message.from_user.id
            user_mention = message.from_user.mention
            user_username = message.from_user.username

        # Construct log message with clear Group and User sections
        logger_text = f"""
<b>{app.mention} ᴘʟᴀʏ ʟᴏɢ</b>

<b>📍 <u>ᴄʜᴀᴛ ɪɴғᴏ :</u></b>
<b>• ɴᴀᴍᴇ :</b> {chat_title}
<b>• ɪᴅ :</b> <code>{chat_id}</code>
<b>• ᴜsᴇʀɴᴀᴍᴇ :</b> @{chat_username if chat_username else "Private/No Username"}

<b>👤 <u>ᴜsᴇʀ ɪɴғᴏ :</u></b>
<b>• ɴᴀᴍᴇ :</b> {user_mention}
<b>• ɪᴅ :</b> <code>{user_id}</code>
<b>• ᴜsᴇʀɴᴀᴍᴇ :</b> @{user_username if user_username else "No Username"}

<b>🎵 <u>sᴛʀᴇᴀᴍ ɪɴғᴏ :</u></b>
<b>• ǫᴜᴇʀʏ :</b> {query}
<b>• ᴛʏᴘᴇ :</b> {streamtype}"""

        if message.chat.id != LOGGER_ID:
            try:
                await app.send_message(
                    chat_id=LOGGER_ID,
                    text=logger_text,
                    parse_mode=ParseMode.HTML,
                    disable_web_page_preview=True,
                )
            except:
                pass
        return
