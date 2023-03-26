import config
from KANNADIGAXD import BOT0, SUDOERS
from telethon import events, Button
from telethon.tl.custom import button
from time import time
from datetime import datetime
 
hl = config.CMD_HNDLR
 
HELP_PIC = "https://telegra.ph/file/5b8d9c29fde33940314bb.jpg"

KANNADIGA_HELP = "🔥 Kᴀɴɴᴀᴅɪɢᴀ XD Bᴏᴛ 🔥\n\n"
 
KANNADIGA_HELP += f"__ᴄᴍɴᴅs ᴀᴠᴀɪʟᴀʙʟᴇ ɪɴ ᴋᴀɴɴᴀᴅɪɢᴀ xᴅ ʙᴏᴛ__\n\n"

KANNADIGA_HELP += f" ↧ sᴘᴀᴍʙᴏᴛ 𝙲𝙼𝙳𝚂 ↧\n\n"

KANNADIGA_HELP += f" `!ping` - to check ping\n `!alive` - to check bot alive/version (only main userbot will reply)\n !`restart` - to restart all spam bots \n `!addecho` - to addecho \n `!rmecho` - To remove Echo \n `!addsudo` - To add sudo user using spam bot \n `!delsudo` to delete someone from sudolist\n\n"
 
KANNADIGA_HELP += f" ↧ 𝙻𝙴𝙰𝚅𝙴 𝙲𝙼𝙳 ↧\n\n"

KANNADIGA_HELP += f" `!leave` - to leave public/private channel/groups\n\n"
 
KANNADIGA_HELP += f" ↧ 𝚂𝙿𝙰𝙼 𝙲𝙼𝙳𝚂 ↧\n\n"

KANNADIGA_HELP += f" `!raid` - to raid\n `!replyraid` - to active reply raid\n `!dreplyraid` - to de-active reply raid\n `!spam` - this cmd use for Normal spam\n `!bigspam` - this cmd use for big spam\n `!bspam` - this cmd use for spamming on someone birthday!!\n `!delayspam` - this cmd use for delay spam\n\n"

KANNADIGA_HELP += f" !kannadigaxd - ɪ ᴡɪʟʟ ꜱᴜɢɢᴇꜱᴛ ᴅᴏɴ'ᴛ ᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ😂 ↧\n\n"

KANNADIGA_HELP += f"© @AGOUTAGORA\n"


@BOT0.on(events.NewMessage(incoming=True, pattern='/help'))
async def help(event):               
    if event.sender_id in SUDOERS:
       blaze = [[Button.url("ᴅᴀᴅᴅʏ👅", "https://t.me/aboutagora"), Button.url("sᴜᴘᴘᴏʀᴛ", "https://t.me/kannadiga_xd")]]
       await BOT0.send_file(event.chat_id, HELP_PIC, caption=KANNADIGA_HELP, buttons=blaze) 
