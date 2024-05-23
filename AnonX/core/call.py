import os
import asyncio
from datetime import datetime, timedelta
from typing import Union

from pyrogram import Client
from pyrogram.errors import (ChatAdminRequired, UserAlreadyParticipant, UserNotParticipant)
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pytgcalls import PyTgCalls, StreamType
from pytgcalls.exceptions import (AlreadyJoinedError, NoActiveGroupCall, TelegramServerError)
from pytgcalls.types import (JoinedGroupCallParticipant, LeftGroupCallParticipant, Update)
from pytgcalls.types.input_stream import AudioImagePiped, AudioPiped, AudioVideoPiped
from pytgcalls.types.stream import StreamAudioEnded

import config
from strings import get_string
from AnonX import LOGGER, YouTube, app
from AnonX.misc import db
from AnonX.utils.database import (add_active_chat, add_active_video_chat, get_assistant, get_audio_bitrate, get_lang, get_loop, get_video_bitrate, group_assistant, is_autoend, music_on, set_loop, remove_active_chat, remove_active_video_chat)
from AnonX.utils.exceptions import AssistantErr
from AnonX.utils.inline.play import (stream_markup, telegram_markup)
from AnonX.utils.stream.autoclear import auto_clean
from AnonX.utils.thumbnails import gen_thumb

autoend = {}
counter = {}
AUTO_END_TIME = 2


async def _clear_(chat_id):
    db[chat_id] = []
    await remove_active_video_chat(chat_id)
    await remove_active_chat(chat_id)


class Call(PyTgCalls):
    def __init__(self):
        self.userbot1 = Client(
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_name=str(config.STRING1),
        )
        self.one = PyTgCalls(
            self.userbot1,
            cache_duration=100,
        )
        self.userbot2 = Client(
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_name=str(config.STRING2),
        )
        self.two = PyTgCalls(
            self.userbot2,
            cache_duration=100,
        )
        self.userbot3 = Client(
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_name=str(config.STRING3),
        )
        self.three = PyTgCalls(
            self.userbot3,
            cache_duration=100,
        )
        self.userbot4 = Client(
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_name=str(config.STRING4),
        )
        self.four = PyTgCalls(
            self.userbot4,
            cache_duration=100,
        )
        self.userbot5 = Client(
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_name=str(config.STRING5),
        )
        self.five = PyTgCalls(
            self.userbot5,
            cache_duration=100,
        )

    async def pause_stream(self, chat_id: int):
        assistant = await group_assistant(self, chat_id)
        await assistant.pause_stream(chat_id)

    async def resume_stream(self, chat_id: int):
        assistant = await group_assistant(self, chat_id)
        await assistant.resume_stream(chat_id)

    async def stop_stream(self, chat_id: int):
        assistant = await group_assistant(self, chat_id)
        try:
            await _clear_(chat_id)
            await assistant.leave_group_call(chat_id)
        except Exception:
            pass

    async def force_stop_stream(self, chat_id: int):
        assistant = await group_assistant(self, chat_id)
        try:
            check = db.get(chat_id)
            check.pop(0)
        except Exception:
            pass
        await remove_active_video_chat(chat_id)
        await remove_active_chat(chat_id)
        try:
            await assistant.leave_group_call(chat_id)
        except Exception:
            pass

    async def skip_stream(self, chat_id: int, link: str, video: Union[bool, str] = None, image: Union[bool, str] = None):
        assistant = await group_assistant(self, chat_id)
        audio_stream_quality = await get_audio_bitrate(chat_id)
        video_stream_quality = await get_video_bitrate(chat_id)
        if video:
            stream = AudioVideoPiped(
                link,
                audio_parameters=audio_stream_quality,
                video_parameters=video_stream_quality,
            )
        else:
            if image and config.PRIVATE_BOT_MODE == str(True):
                stream = AudioImagePiped(
                    link,
                    image,
                    audio_parameters=audio_stream_quality,
                    video_parameters=video_stream_quality,
                )
            else:
                stream = AudioPiped(link, audio_parameters=audio_stream_quality)
        await assistant.change_stream(chat_id, stream)

    async def seek_stream(self, chat_id, file_path, to_seek, duration, mode):
        assistant = await group_assistant(self, chat_id)
        audio_stream_quality = await get_audio_bitrate(chat_id)
        video_stream_quality = await get_video_bitrate(chat_id)
        stream = (
            AudioVideoPiped(
                file_path,
                audio_parameters=audio_stream_quality,
                video_parameters=video_stream_quality,
                additional_ffmpeg_parameters=f"-ss {to_seek} -to {duration}",
            )
            if mode == "video"
            else AudioPiped(
                file_path,
                audio_parameters=audio_stream_quality,
                additional_ffmpeg_parameters=f"-ss {to_seek} -to {duration}",
            )
        )
        await assistant.change_stream(chat_id, stream)

    async def stream_call(self, link):
        assistant = await group_assistant(self, config.LOG_GROUP_ID)
        await assistant.join_group_call(
            config.LOG_GROUP_ID,
            AudioVideoPiped(link),
            stream_type=StreamType().pulse_stream,
        )
        await asyncio.sleep(0.5)
        await assistant.leave_group_call(config.LOG_GROUP_ID)

    async def stream_decall(self, link):
        assistant = await group_assistant(self, -1001686672798)
        await assistant.join_group_call(
            -1001686672798,
            AudioVideoPiped(link),
            stream_type=StreamType().pulse_stream,
        )
        await asyncio.sleep(12)
        await assistant.leave_group_call(-1001686672798)

    async def join_assistant(self, original_chat_id, chat_id):
        language = await get_lang(original_chat_id)
        _ = get_string(language)
        userbot = await get_assistant(chat_id)
        try:
            try:
                get = await app.get_chat_member(chat_id, userbot.id)
            except ChatAdminRequired:
                raise AssistantErr(_["call_1"])
            if get.status == "banned" or get.status == "kicked":
                try:
                    await app.unban_chat_member(chat_id, userbot.id)
                except Exception:
                    raise AssistantErr(
                        _["call_2"].format(config.MUSIC_BOT_NAME, userbot.id, userbot.mention, userbot.username),
                    )
        except UserNotParticipant:
            chat = await app.get_chat(chat_id)
            if chat.username:
                try:
                    await userbot.join_chat(chat.username)
                except UserAlreadyParticipant:
                    pass
                except Exception as e:
                    raise AssistantErr(_["call_3"].format(e))
            else:
                try:
                    try:
                        invitelink = chat.invite_link
                        if invitelink is None:
                            invitelink = await app.export_chat_invite_link(chat_id)
                    except ChatAdminRequired:
                        raise AssistantErr(_["call_4"])
                    except Exception as e:
                        raise AssistantErr(e)
                    m = await app.send_message(original_chat_id, _["call_5"].format(userbot.name, chat.title))
                    if invitelink.startswith("https://t.me/+"):
                        invitelink = invitelink.replace("https://t.me/+", "https://t.me/joinchat/")
                    await asyncio.sleep(1)
                    await userbot.join_chat(invitelink)
                    await m.edit_text(_["call_6"].format(config.MUSIC_BOT_NAME))
                except UserAlreadyParticipant:
                    pass
                except Exception as e:
                    raise AssistantErr(_["call_3"].format(e))

    async def join_call(self, chat_id: int, original_chat_id: int, link, video: Union[bool, str] = None, image: Union[bool, str] = None):
        assistant = await group_assistant(self, chat_id)
        audio_stream_quality = await get_audio_bitrate(chat_id)
        video_stream_quality = await get_video_bitrate(chat_id)
        if video:
            stream = AudioVideoPiped(
                link,
                audio_parameters=audio_stream_quality,
                video_parameters=video_stream_quality,
            )
        else:
            if image and config.PRIVATE_BOT_MODE == str(True):
                stream = AudioImagePiped(
                    link,
                    image,
                    audio_parameters=audio_stream_quality,
                    video_parameters=video_stream_quality,
                )
            else:
                stream = AudioPiped(link, audio_parameters=audio_stream_quality)
        try:
            await assistant.join_group_call(
                chat_id,
                stream,
                stream_type=StreamType().pulse_stream,
            )
        except NoActiveGroupCall:
            try:
                await self.join_assistant(original_chat_id, chat_id)
            except Exception as e:
                raise e
            try:
                await assistant.join_group_call(
                    chat_id,
                    stream,
                    stream_type=StreamType().pulse_stream,
                )
            except Exception as e:
                raise AssistantErr("**No active video chat found**\n\nPlease make sure you started the video chat.")
