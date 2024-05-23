import sys
from pyrogram import Client, errors
import config
from ..logging import LOGGER

class AnonXBot(Client):
    def __init__(self):
        self.logger = LOGGER(__name__)
        self.logger.info("Starting Bot...")
        super().__init__(
            "AnonXMusic",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
        )

    async def start(self):
        await super().start()
        try:
            get_me = await self.get_me()
            self.username = get_me.username
            self.id = get_me.id
            self.name = f"{get_me.first_name} {get_me.last_name}" if get_me.last_name else get_me.first_name

            a = await self.get_chat_member(config.LOG_GROUP_ID, self.id)
            if a.status != "administrator":
                self.logger.error("Please promote Bot as Admin in Logger Group")
                await self.stop()
                sys.exit()

            self.logger.info(f"MusicBot Started as {self.name}")
            try:
                await self.send_message(
                    config.LOG_GROUP_ID,
                    f"**» {config.MUSIC_BOT_NAME} 𝐁𝐨𝐭 𝐒𝐭𝐚𝐫𝐭𝐞𝐝 𝐛𝐚𝐛𝐲🤩 **\n\n✨ 𝐈𝐃 : `{self.id}`\n🥰𝐍𝐀𝐌𝐄 : {self.name}\n💫 𝐔𝐒𝐄𝐑𝐍𝐀𝐌𝐄 : @{self.username}"
                )
            except errors.Forbidden as e:
                self.logger.error(
                    f"Bot has failed to access the log Group. Make sure that you have added your bot to your log channel and promoted as admin! Error: {e}"
                )
                await self.stop()
                sys.exit()
        except Exception as e:
            self.logger.error(f"An error occurred during bot start: {e}")
            await self.stop()
            sys.exit()

    async def run(self):
        await self.start()
        await idle()  # Wait until interrupt signal

if __name__ == "__main__":
    bot = AnonXBot()
    bot.run()
