import config
from KANNADIGAXD import BOT0, deadlyversion, SUDOERS
from telethon import events, version, Button
from telethon.tl.custom import button

PIC = config.ALIVE_PIC

if config.ALIVE_PIC:
    KANNADIGA_PIC = PIC
else:
    KANNADIGA_PIC = "https://telegra.ph/file/5b8d9c29fde33940314bb.jpg"

hl = config.CMD_HNDLR


KANNADIGA = "✯ KANNADIGA XD SPAM ✯\n\n"
KANNADIGA += f"═══════════════════\n"
KANNADIGA += f"• **PYTHON XD** : `4.0.0`\n"
KANNADIGA += f"• **TELETHON XD** : `{version.__version__}`\n"
KANNADIGA += f"• **KANNADIGA XD**  : `{deadlyversion}`\n"
KANNADIGA += f"═══════════════════\n\n"   


@BOT0.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
async def alive(event): 
  if event.sender_id in SUDOERS:
     Blaze = [[Button.url("ᴄʜᴀɴɴᴇʟ", "https://t.me/ABOUTAGORA"), Button.url("sᴜᴘᴘᴏʀᴛ", "https://t.me/DO_JISM_EK_JAAN_OP")], [Button.url("• ʀᴇᴘᴏ •", "https://github.com/kannadigaXD/Spambot")]]
     await BOT0.send_file(event.chat_id, KANNADIGA_PIC, caption=KANNADIGA, buttons=Blaze) 
  else:
      await event.reply("**kannadiga xd bots are ready!**") 
