import sys
from pyrogram import Client
import config
from ..logging import LOGGER

assistants = []
assistantids = []

class Userbot:
    def __init__(self):
        self.clients = []
        for string in [config.STRING1, config.STRING2, config.STRING3, config.STRING4, config.STRING5]:
            if string:
                client = Client(
                    name=str(string),
                    api_id=config.API_ID,
                    api_hash=config.API_HASH,
                    no_updates=True,
                )
                self.clients.append(client)

    async def start(self):
        LOGGER(__name__).info("Getting Assistants Info...")
        for i, client in enumerate(self.clients, start=1):
            try:
                await client.start()
                try:
                    await client.join_chat("TG_FRIENDSS")
                    await client.join_chat("VIP_CREATORS")
                except:
                    pass
                assistants.append(i)
                get_me = await client.get_me()
                client.username = get_me.username
                client.id = get_me.id
                client.mention = get_me.mention
                assistantids.append(get_me.id)
                if get_me.last_name:
                    client.name = f"{get_me.first_name} {get_me.last_name}"
                else:
                    client.name = get_me.first_name
                LOGGER(__name__).info(f"Assistant {i} Started as {client.name}")
                try:
                    await client.send_message(
                        config.LOG_GROUP_ID,
                        f"**» {config.MUSIC_BOT_NAME} ᴀssɪsᴛᴀɴᴛ {i} sᴛᴀʀᴛᴇᴅ :**\n\n✨ ɪᴅ : `{client.id}`\n❄ ɴᴀᴍᴇ : {client.name}\n💫 ᴜsᴇʀɴᴀᴍᴇ : @{client.username}"
                    )
                except:
                    LOGGER(__name__).error(
                        f"Assistant Account {i} has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin!"
                    )
                    sys.exit()
            except Exception as e:
                LOGGER(__name__).error(f"Error starting Assistant {i}: {e}")
                sys.exit()
