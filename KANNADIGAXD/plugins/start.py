import os
import asyncio
import config
from telethon import events, Button
from telethon.tl.custom import button
from KANNADIGAXD import BOT0, BOT1, BOT2, BOT3, BOT4, BOT5, BOT6, BOT7, BOT8, BOT9

ALIVE_IMG = config.ALIVE_PIC

if config.ALIVE_PIC:
    KANNADIGA_IMG = ALIVE_IMG
else:
    KANNADIGA_IMG = "https://telegra.ph/file/5b8d9c29fde33940314bb.jpg"

OWNER_INFO = config.OWNER_NAME
if config.OWNER_NAME:
    OWNER_NAME = OWNER_INFO
else:
    OWNER_NAME = "KARANADU KING"

OWNER_ID = config.OWNER_ID

KannadigaXD_Button = [
        [
        Button.url("Cʜᴀɴɴᴇʟ", "https://t.me/ABOUT_SHAAN"),
        Button.url("Sᴜᴘᴘᴏʀᴛ", "https://t.me/KARUNADA_KINGS_KINGDOM")
        ],
        [
        Button.url("• Rᴇᴘᴏ •", "https://t.me/KARUNADAKING")
        ]
        ]
        

#USERS 


@BOT0.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT1.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT2.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT3.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT4.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT5.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT6.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT7.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT8.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT9.on(events.NewMessage(incoming=True, pattern='/start'))
async def start(e):
    if e.chat_id is e.sender_id:
        name = e.sender.first_name
        user_id = e.sender_id
        mention = f"[{name}](tg://user?id={user_id})"
        myOwner = f"[{OWNER_NAME}](tg://user?id={OWNER_ID})"
        creator = f"[ᴅᴀᴅᴅʏ👅](tg://user?id={8432556224})"
        KANNADIGA_ON = f"""
ʜᴇʏ {mention},
ᴛʜɪs ɪs ᴋᴀɴɴᴀᴅɪɢᴀ xᴅ sᴘᴀᴍʙᴏᴛ ᴘᴏᴡᴇʀᴇᴅ ʙʏ:- {creator}!

ᴛʜɪs ʙᴏᴛ ᴏᴡɴᴇʀ:- {myOwner}

ᴄᴏᴅᴇ ᴄʀᴇᴀᴛᴏʀ:- {creator}

ᴄʟɪᴄᴋ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ ᴛᴏ ᴀᴄᴄᴇss sᴜᴘᴘᴏʀᴛ ,ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ʀᴇᴘᴏ!
    """
        await e.client.send_file(e.chat_id, KANNADIGA_IMG, caption=KANNADIGA_ON, buttons=KannadigaXD_Button)
