from datetime import datetime
from typing import Union
from pyrogram import filters
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import BANNED_USERS, MUSIC_BOT_NAME, PING_IMG_URL
import config
from strings import get_command
from AnonX import app
from AnonX.core.call import Anon
from AnonX.utils import bot_sys_stats
from AnonX.utils.decorators.language import language
from AnonX.utils.inline.play import close_keyboard
from AnonX.utils.inline.core.bot.start 
### Commands
PING_COMMAND = get_command("PING_COMMAND")


@app.on_message(
    filters.command(PING_COMMAND)
)
@language
async def ping_com(client, message: Message, _):
    response = await message.reply_photo(
        photo=PING_IMG_URL, 
        caption=_["ping_1"],
    )
    start = datetime.now()
    pytgping = await Vip.ping()
    UP, CPU, RAM, DISK = await bot_sys_stats()
    resp = (datetime.now() - start).microseconds / 1000
    await response.edit_text(
        _["ping_3"])
    await response.edit_text(
        _["ping_4"])
    await response.edit_text(
        _["ping_2"].format(
            resp, MUSIC_BOT_NAME, UP, RAM, CPU, DISK, pytgping
        ))
    await response.edit_text(
       _["ping_5"].format(
            resp, MUSIC_BOT_NAME, UP, RAM, CPU, DISK, pytgping
        ))
    await response.edit_text(
        _["ping_6"].format(
            resp, MUSIC_BOT_NAME, UP, RAM, CPU, DISK, pytgping
        ))
    await response.edit_text(
        _["ping_7"].format(
            resp, MUSIC_BOT_NAME, UP, RAM, CPU, DISK, pytgping
        ))
    await response.edit_text(
        _["ping_8"].format(
            resp, MUSIC_BOT_NAME, UP, RAM, CPU, DISK, pytgping
        ))
    await response.edit_text(
        _["ping_9"].format(
            resp, MUSIC_BOT_NAME, UP, RAM, CPU, DISK, pytgping
        ))
    await response.edit_text(
        _["ping_10"].format(
            resp, MUSIC_BOT_NAME, UP, RAM, CPU, DISK, pytgping
        ))
    await response.edit_text(
        _["ping_11"].format(
            resp, MUSIC_BOT_NAME, UP, RAM, CPU, DISK, pytgping
        ))
    await response.edit_text(
        _["ping_12"].format(
            resp, MUSIC_BOT_NAME, UP, RAM, CPU, DISK, pytgping
        ),
        reply_markup=InlineKeyboardMarkup(
            [
                [
            InlineKeyboardButton(
                text="💋ᴋɪss ᴍᴇ ʙᴀʙʏ💋",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        
        ],
        [
            InlineKeyboardButton(
                text="🌸ᴄʜᴀᴛ ɢʀᴏᴜᴘ🌸", url=f"https://t.me/Hindi_Marathi_Friends_Group",
            ),
            InlineKeyboardButton(
                text="🍎ᴀᴘᴘʟᴇ ᴍᴜsɪᴄ🍎", url=f"http://t.me/Govind2_musicsbot",
            )
        ],
        [
            InlineKeyboardButton(
                text="⚙️ 𝐇𝐄𝐋𝐏 ⚙️", callback_data="settings_back_helper"
            )
        ],
    ]
    ),
)
    
        
