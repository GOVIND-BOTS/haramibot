import asyncio
import random

from AnonX import *

RAID_STR = [
    "HAYEE MERI JAAN ðŸ¤©ðŸ¤©",
    "MERI JAAN KITNI OSM HAI YAAR ðŸ˜ðŸŒ¹ðŸŒ¹ðŸ˜ðŸ˜ðŸ˜",
    "I LOVE YOU MERI JAAN â¤ï¸â¤ï¸",
    "MERI JAAN I KISS YOU â¤ï¸ðŸ˜‹ðŸ˜ŠðŸ˜˜ðŸ˜˜ðŸ˜˜",
    "I MISS YOU JAAN ðŸ¥€ðŸ¥€âœ¨âœ¨",
    "Mat muskurao itna ki Phoolo ko khabar lag jaye Ke wo kare taaref tumhari Aur tumhe unki najar lag jaye",
    "Chand se haseen hai chandni Chandni se haseen hai Raat Raat se haseen hai chand Aur chand se haseen hai aap",
 "You look so beautiful and pretty I feel lucky because you love me I love you now and Iâ€™ll always do Because I just canâ€™t live without you",
 "Chand sa tera masoom chehra Tu haya ki ek murat hai Tujhe dekh ke kaliya bhi sharmaaye Tu itni khoobsurat hai", 
 "à¤•à¥ˆà¤¸à¥‡ à¤•à¤°à¥à¤‚ à¤¬à¤¯à¤¾à¤ à¤®à¥ˆ à¤–à¥à¤¬à¤¸à¥à¤°à¤¤à¥€ à¤‰à¤¸à¤•à¥€ à¤®à¥‡à¤¨à¥‡ à¤¤à¥‹ à¤‰à¤¸à¥‡ à¤¬à¤¿à¤¨à¤¾ à¤¦à¥‡à¤–à¥‡ à¤¹à¥€ à¤ªà¥à¤¯à¤¾à¤° à¤•à¤¿à¤¯à¤¾ à¤¹à¥ˆà¥¤", 
 "Mai tumhari sadagi ki kya misal du Is saare jaha me Be misaal ho tum",
 " LOVE YOU JAAN ðŸ˜ðŸ˜ðŸ”¥ðŸ”¥ðŸ˜‚",
 "I HUG YOU BABY ðŸ¤£ðŸ¤£",
 " I LOVE YOU SO MUCH ðŸŒ¹ðŸ’«ðŸ’–",
 "MADE BY DEV JAAN ðŸ˜‚ðŸ˜‚",
 "Ð½ello ðŸ˜Ð¼erÎ¹ jaan",
 "oye Ð²aÐ²y Ñ•Ï…no na ðŸ˜",
 "Î¹ love Ï… Ð²aÐ²eðŸ˜˜",
 "Ñ‚Ï…Ð¼ Ð½Î¹ Ð½oðŸ¥ºâ¤ï¸",
 "à¤†à¤ª à¤¹à¥€ à¤•à¥‡ à¤¬à¤¿à¤¨à¤¾ à¤¹à¤® à¤•à¥à¤¯à¥‹à¤‚ à¤¬à¥‡à¤šà¥ˆà¤¨ à¤¹à¥ˆà¤‚",
"à¤†à¤ª à¤¹à¥€ à¤•à¥à¤¯à¥‹à¤‚ à¤®à¥‡à¤°à¥€ à¤œà¤°à¥‚à¤°à¤¤ à¤¹à¥ˆà¤‚",
"à¤µà¤¹à¤® à¤‡à¤¤à¤¨à¤¾ à¤¹à¤¸à¥€à¤‚ à¤¨à¤¹à¥€à¤‚ à¤¹à¥‹à¤¤à¤¾",
"à¤µà¤¾à¤•à¤ˆ à¤†à¤ª à¤–à¥‚à¤¬à¤¸à¥‚à¤°à¤¤ à¤¹à¥ˆà¤‚",
"á´yá´‡ Êœá´yá´‡ êœ±á´€Ê€á´á´€ É¢yÉª á´‹á´€á´€ á´©Êœá´É´á´‡ á´‹á´€á´› á´…Éª á´á´œá´á´y á´€á´€ É¢yÉª á´‹yá´€ ðŸ¤£",
" TU MAAN MERI JAAN TUJHE JANE NA DUNGA ðŸ¤£ðŸ¤£âœ¨",
"TUJHE APNI BAHO ME SAJAKE ðŸ¤£ðŸ¤£ðŸ¤£",
"EK UCHA LMBA KAD DUJA SONI HONI HAD TIJHA TERA RUP CHAM CHAM KR DANI TERE SIVHA DIL ME KOI UTRA THA NHIðŸ¤£ðŸ¤£ðŸ¤£ðŸ¤£ðŸŒ¹ðŸŒ¹",
"BS KHAFI HO GYI JHUT KI TARIFðŸ¤£ðŸ¤£ðŸ¤£",
"HEY HA YOU....YOU ARE SO BEAUTIFUL âœ¨ðŸŒ¹ I LOVE YOU ðŸ¤£ðŸ¥€ðŸ¥€ðŸ¥€âœ¨âœ¨ðŸŒ¹ðŸŒ¹",
"MERI JAAN TUJHE NAZAR NA ðŸ¤£LGA JAYE KISI KI ðŸ™„ðŸ†˜",
" KIN NA SONA TUJHE RAB NE BNAYA KI JI KRE DEKH THA RHU ðŸ˜‚ðŸ˜‚ðŸŒ¹ðŸŒ¹â¤ï¸â¤ï¸ðŸ˜œðŸ¤£ðŸ¤£",
"LAL DUPATTA UD GYA  HAYE MERI BEAUTY SE ðŸ¤£ðŸ¤£ðŸ˜œðŸ˜œ",
"BS BS HO GYI AB JHUTI TARIF JAAN ðŸ¤£ðŸ¤£ðŸ¤£",
"#LOVE YOU JAAN",
"I WANT YOU ðŸ‘€BABY",
" UMMMMM MAAA MERI JAAN ðŸ˜ðŸ˜˜ðŸ˜˜ðŸ˜˜ðŸ˜˜ðŸ˜˜",
]

que = {}


@app.on_message_handler()
async def _(event):
    global que
    queue = que.get(event.sender_id)
    if not queue:
        return
    async with event.client.action(event.chat_id, "typing"):
        await asyncio.sleep(0.3)
    async with event.client.action(event.chat_id, "typing"):
        await event.client.send_message(
            entity=event.chat_id,
            message="""{}""".format(random.choice(RAID_STR)),
            reply_to=event.message.id,
        )

@app.on_message_cmd(pattern="loveraid(?:\s|$)([\s\S]*)")
async def _(event):
    global que
    if event.fwd_from:
        return
    if event.reply_to_msg_id:
        a = await event.get_reply_message()
        b = await event.client.get_entity(a.sender_id)
        e = b.id
        c = b.first_name
        username = f"[{c}](tg://user?id={e})"
        event = await eor(event, "love Activating....")
        que[e] = []
        qeue = que.get(e)
        appendable = [e]
        qeue.append(appendable)
        await event.edit(f"love has been activated on {username}")
    else:
        user = event.pattern_match.group(1)
        event = await eor(event, "love Activating....")
        a = await event.client.get_entity(user)
        e = a.id
        c = a.first_name
        username = f"[{c}](tg://user?id={e})"
        que[e] = []
        qeue = que.get(e)
        appendable = [e]
        qeue.append(appendable)
        await event.edit(f"love has been activated on {username}")


@app.on_message_cmd(pattern="dlove(?:\s|$)([\s\S]*)")
async def _(event):
    global que
    if event.fwd_from:
        return
    if event.reply_to_msg_id:
        a = await event.get_reply_message()
        b = await event.client.get_entity(a.sender_id)
        e = b.id
        c = b.first_name
        username = f"[{c}](tg://user?id={e})"
        event = await eor(event, "love De-activating....")
        queue = que.get(e)
        queue.pop(0)
        await event.edit(f"love has been De-activated on {username}")
    else:
        user = event.pattern_match.group(1)
        event = await eor(event, "love De-activating....")
        a = await event.client.get_entity(user)
        e = a.id
        c = a.first_name
        username = f"[{c}](tg://user?id={e})"
        queue = que.get(e)
        queue.pop(0)
        await event.edit(f"love has been De-activated on {username}")

CmdHelp("loveraid").add_command(
    "devlove", None, "Starts  love on mentioned user."
).add_command(
    "dlove", None, "Stops  love on mentioned user."
).add_warning(
    "May get floodwait!"
).add_info(
    "AnonX Module"
).add()
