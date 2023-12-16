from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="☆ 𝗸𝗶𝗱𝗻𝗮𝗽 𝐌𝐞 𝐌𝐨𝐢 𝐋𝐮𝐯 ☆",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="🎭 𝐇𝐞𝐥𝐩 🎭",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="🕹️ 𝐒𝐞𝐭𝐭𝐢𝐧𝐠𝐬 🕹️", callback_data="settings_helper"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="☆ 𝗸𝗶𝗱𝗻𝗮𝗽 𝗺𝗲 𝗺𝗼𝗶 𝗹𝗼𝗯 ☆",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="📍𝐎𝐰𝐧𝐞𝐫📍", user_id=OWNER
            ),
            InlineKeyboardButton(
                text="🎭 𝐇𝐞𝐥𝐩 🎭", callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="🍒𝐆𝐫𝐨𝐮𝐩🍒", url=config.SUPPORT_GROUP
            ),
            InlineKeyboardButton(
                text="🙃𝐋𝐨𝐯𝐞 𝐟𝐢𝐥𝐥𝐢𝐧𝐠", url=f"https://t.me/online_love_fillings",
            )
        ],
        [
            InlineKeyboardButton(
                text="🌱𝗣𝗢𝗥𝗘🌱",
                url=f"https://github.com/GOVIND-BOTS/haramibot",
            )
        ],
     ]
    return buttons
