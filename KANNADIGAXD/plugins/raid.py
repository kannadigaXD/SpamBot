
import asyncio
import base64
import os
import random        
import config
from telethon import events
from telethon import functions, types
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from resources.data import RAID, REPLYRAID, DEADLYSPAM, BRTHSPAM
from DEADLYSPAM import BOT0, BOT1, BOT2, BOT3, BOT4, BOT5, BOT6, BOT7, BOT8, BOT9, SUDOERS


hl = config.CMD_HNDLR 


que = {}


@BOT0.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@BOT1.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@BOT2.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@BOT3.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@BOT4.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@BOT5.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@BOT6.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@BOT7.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@BOT8.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@BOT9.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗥𝗮𝗶𝗱\n\nCommand:\n\n.raid <count> <Username of User>\n\n.raid <count> <reply to a User>\n\nCount must be a integer."
    if e.sender_id in SUDOERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage)
        Deadly = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        bitxh = await e.get_reply_message()
        if len(Deadly) == 2:
            user = str(Deadly[1])
            a = await e.client.get_entity(user)
            g = a.id
            if int(g) in DEADLYSPAM:
                text = f"» ᴄᴀɴɴᴏᴛ ʀᴀɪᴅ ᴏɴ ᴅᴇᴀᴅʟʏ ᴄʀᴇᴀᴛᴏʀ !"
                await e.reply(text)
            elif int(g) == config.OWNER_ID:
                text = f"» ɪ  ᴄᴀɴɴᴏᴛ ʀᴀɪᴅ ᴏɴ ᴍʏ ᴏᴡɴᴇʀ  !"
                await e.reply(text)
            elif int(g) in SUDOERS:
                text = f"» ᴄᴀɴɴᴏᴛ ʀᴀɪᴅ ᴏɴ ꜱᴜᴅᴏᴇʀ !"
                await e.reply(text) 
            else:
                c = a.first_name
                username = f"[{c}](tg://user?id={g})"
                counter = int(Deadly[0])
                for _ in range(counter):
                    reply = random.choice(RAID)
                    caption = f"{username} {reply}"
                    async with e.client.action(e.chat_id, "typing"):
                        await e.client.send_message(e.chat_id, caption)
                        await asyncio.sleep(0.5)
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            if int(g) in DEADLYSPAM:
                text = f"» ᴄᴀɴɴᴏᴛ ʀᴀɪᴅ ᴏɴ ᴅᴇᴀᴅʟʏ ᴄʀᴇᴀᴛᴏʀ !"
                await e.reply(text)
            elif int(g) == config.OWNER_ID:
                text = f"» ɪ  ᴄᴀɴɴᴏᴛ ʀᴀɪᴅ ᴏɴ ᴍʏ ᴏᴡɴᴇʀ  !"
                await e.reply(text)
            elif int(g) in SUDOERS:
                text = f"» ᴄᴀɴɴᴏᴛ ʀᴀɪᴅ ᴏɴ ꜱᴜᴅᴏᴇʀ !"
                await e.reply(text)
            else:
                c = b.first_name
                counter = int(Deadly[0])
                username = f"[{c}](tg://user?id={g})"
                for _ in range(counter):
                    reply = random.choice(RAID)
                    caption = f"{username} {reply}"
                    async with e.client.action(e.chat_id, "typing"):
                        await e.client.send_message(e.chat_id, caption)
                        await asyncio.sleep(0.3)
        else:
            await e.reply(usage)



@BOT0.on(events.NewMessage(incoming=True))
@BOT1.on(events.NewMessage(incoming=True))
@BOT2.on(events.NewMessage(incoming=True))
@BOT3.on(events.NewMessage(incoming=True))
@BOT4.on(events.NewMessage(incoming=True))
@BOT5.on(events.NewMessage(incoming=True))
@BOT6.on(events.NewMessage(incoming=True))
@BOT7.on(events.NewMessage(incoming=True))
@BOT8.on(events.NewMessage(incoming=True))
@BOT9.on(events.NewMessage(incoming=True))
async def _(event):
    global que
    queue = que.get(event.sender_id)
    if not queue:
        return
    async with event.client.action(event.chat_id, "typing"):
        await asyncio.sleep(0.2)
    async with event.client.action(event.chat_id, "typing"):
        await event.client.send_message(
            entity=event.chat_id,
            message="""{}""".format(random.choice(REPLYRAID)),
            reply_to=event.message.id,
        )


@BOT0.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
@BOT1.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
@BOT2.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
@BOT3.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
@BOT4.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
@BOT5.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
@BOT6.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
@BOT7.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
@BOT8.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
@BOT9.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
async def _(e):
    global que
    usage = f"𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗥𝗲𝗽𝗹𝘆𝗥𝗮𝗶𝗱\n\nCommand:\n\n.replyraid <Username of User>\n\n.replyraid <reply to a User>."
    if e.sender_id in SUDOERS:
        Deadly = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        SAMx = await e.get_reply_message()
        if len(e.text) > 11:
            message = str(Deadly[0])
            a = await e.client.get_entity(message)
            user_idd = a.id
            user_id = int(user_idd)
            if int(user_id) in DEADLYSPAM:
                text = f"**» ᴄᴀɴɴᴏᴛ ʀᴀɪᴅ ᴏɴ ᴅᴇᴀᴅʟʏ ᴄʀᴇᴀᴛᴏʀ !**"
                await e.reply(text)
            elif int(user_id) == config.OWNER_ID:
                text = f"» ɪ  ᴄᴀɴɴᴏᴛ ʀᴀɪᴅ ᴏɴ ᴍʏ ᴏᴡɴᴇʀ  !"            
                await event.reply(text)
            elif int(user_id) in SUDOERS:
                text = f"» ᴄᴀɴɴᴏᴛ ʀᴀɪᴅ ᴏɴ ꜱᴜᴅᴏᴇʀ !"
                await e.reply(text)
            else:
                que[user_id] = []
                gey = que.get(user_id)
                phucker = [user_id]
                gey.append(phucker)
                text = f"**ʀᴇᴘʟʏʀᴀɪᴅ ᴀᴄᴛɪᴠᴀᴛᴇᴅ** !"
                await e.reply(text)
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            umser = await e.client.get_entity(a.sender_id)
            user_idd = umser.id
            user_id = int(user_idd)
            if int(user_id) in DEADLYSPAM:
                text = f" » ᴄᴀɴɴᴏᴛ ʀᴀɪᴅ ᴏɴ ᴅᴇᴀᴅʟʏ ᴄʀᴇᴀᴛᴏʀ !"
                await e.reply(text)
            elif int(user_id) == config.OWNER_ID:
                text = f"» ɪ  ᴄᴀɴɴᴏᴛ ʀᴀɪᴅ ᴏɴ ᴍʏ ᴏᴡɴᴇʀ !"
                await event.reply(text)
            elif int(user_id) in SUDOERS:
                text = f"» ᴄᴀɴɴᴏᴛ ʀᴀɪᴅ ᴏɴ ꜱᴜᴅᴏᴇʀ !"
                await e.reply(text)
            else:
                que[user_id] = []
                gey = que.get(user_id)
                phucker = [user_id]
                gey.append(phucker)
                text = f"**ʀᴇᴘʟʏʀᴀɪᴅ ᴀᴄᴛɪᴠᴀᴛᴇᴅ** !"
                await e.reply(text)
        else:
            await e.reply(usage)


@BOT0.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl))
@BOT1.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl))
@BOT2.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl))
@BOT3.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl))
@BOT4.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl))
@BOT5.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl))
@BOT6.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl))
@BOT7.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl))
@BOT8.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl))
@BOT9.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl))
async def _(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗗𝗲𝗮𝗰𝘁𝗶𝘃𝗮𝘁𝗲 𝗥𝗲𝗽𝗹𝘆𝗥𝗮𝗶𝗱\n\nCommand:\n\n.dreplyraid <Username of User>\n\n.dreplyraid <reply to a User>"
    global que    
    if e.sender_id in SUDOERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage)
        Deadly = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(e.text) > 12:
            message = str(Deadly[0])
            a = await e.client.get_entity(message)
            g = a.id
            try:
                queue = que.get(g)
                queue.pop(0)
            except Exception as f:
                pass
            text = "**ʀᴇᴘʟʏʀᴀɪᴅ ᴅᴇ-ᴀᴄᴛɪᴠᴀᴛᴇᴅ** !"
            await e.reply(text)
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            try:
                queue = que.get(g)
                queue.pop(0)
            except Exception as f:
                pass
            text = "**ʀᴇᴘʟʏʀᴀɪᴅ ᴅᴇ-ᴀᴄᴛɪᴠᴀᴛᴇᴅ** !"
            await e.reply(text)
        else:
            await e.reply(usage)
    
@BOT0.on(events.NewMessage(incoming=True, pattern=r"\%sdelayraid(?: |$)(.*)" % hl))
@BOT1.on(events.NewMessage(incoming=True, pattern=r"\%sdelayraid(?: |$)(.*)" % hl))
@BOT2.on(events.NewMessage(incoming=True, pattern=r"\%sdelayraid(?: |$)(.*)" % hl))
@BOT3.on(events.NewMessage(incoming=True, pattern=r"\%sdelayraid(?: |$)(.*)" % hl))
@BOT4.on(events.NewMessage(incoming=True, pattern=r"\%sdelayraid(?: |$)(.*)" % hl))
@BOT5.on(events.NewMessage(incoming=True, pattern=r"\%sdelayraid(?: |$)(.*)" % hl))
@BOT6.on(events.NewMessage(incoming=True, pattern=r"\%sdelayraid(?: |$)(.*)" % hl))
@BOT7.on(events.NewMessage(incoming=True, pattern=r"\%sdelayraid(?: |$)(.*)" % hl))
@BOT8.on(events.NewMessage(incoming=True, pattern=r"\%sdelayraid(?: |$)(.*)" % hl))
@BOT9.on(events.NewMessage(incoming=True, pattern=r"\%sdelayraid(?: |$)(.*)" % hl))
async def _(event):
   usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗗𝗘𝗟𝗔𝗬𝗥𝗔𝗜𝗗\n\nCommand:\n\n.delayraid <delay> <count> <Username of User>\n\n.delayraid <delay> <count> <reply to a User>\n\nCount and Sleeptime must be a integer."        
   if event.sender_id in SUDOERS:
         if event.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
         Deadly = "".join(event.text.split(maxsplit=1)[1:]).split(" ", 2)
         if len(Deadly) == 3:
             user = str(Deadly[2])
             a = await event.client.get_entity(user)
             e = a.id
             if int(e) in DEADLYSPAM:
                 text = f"**» ᴄᴀɴɴᴏᴛ ʀᴀɪᴅ ᴏɴ ᴅᴇᴀᴅʟʏ ᴄʀᴇᴀᴛᴏʀ !**"
                 await event.reply(text)
             elif int(e) == config.OWNER_ID:
                 text = f"**» ɪ  ᴄᴀɴɴᴏᴛ ʀᴀɪᴅ ᴏɴ ᴍʏ ᴏᴡɴᴇʀ  !**"
                 await event.reply(text)
             elif int(e) in SUDOERS:
                 text = f"ᴄᴀɴɴᴏᴛ ʀᴀɪᴅ ᴏɴ ꜱᴜᴅᴏᴇʀ"
                 await event.reply(text)
             else:
                 c = a.first_name
                 username = f"[{c}](tg://user?id={e})"
                 counter = int(Deadly[1])
                 sleeptimet = sleeptimem = float(Deadly[0])
                 for _ in range(counter):
                      reply = random.choice(RAID)
                      caption = f"{username} {reply}"
                      async with event.client.action(event.chat_id, "typing"):
                          await event.client.send_message(event.chat_id, caption)
                          await asyncio.sleep(sleeptimem)
         elif event.reply_to_msg_id:
               a = await event.get_reply_message()
               b = await event.client.get_entity(a.sender_id)
               e = b.id
               if int(e) in DEADLYSPAM:
                   text = f"**» ᴄᴀɴɴᴏᴛ ʀᴀɪᴅ ᴏɴ ᴅᴇᴀᴅʟʏ ᴄʀᴇᴀᴛᴏʀ !**"
                   await event.reply(text)
               elif int(e) == config.OWNER_ID:
                   text = f"**» ɪ  ᴄᴀɴɴᴏᴛ ʀᴀɪᴅ ᴏɴ ᴍʏ ᴏᴡɴᴇʀ  !**"
                   await event.reply(text)
               elif int(e) in SUDOERS:
                   text = f"ᴄᴀɴɴᴏᴛ ʀᴀɪᴅ ᴏɴ ꜱᴜᴅᴏᴇʀ"
                   await event.reply(text)
               else:
                   c = b.first_name
                   username = f"[{c}](tg://user?id={e})"
                   sleeptimet = sleeptimem = float(Deadly[0])
                   counter = int(Deadly[1])
                   for _ in range(counter):
                        reply = random.choice(RAID)
                        caption = f"{username} {reply}"
                        async with event.client.action(event.chat_id, "typing"):
                             await event.client.send_message(event.chat_id, caption)
                             await asyncio.sleep(sleeptimem)
         else:
            await event.reply(usage)


@BOT0.on(events.NewMessage(incoming=True, pattern=r"\%sbspam(?: |$)(.*)" % hl))
@BOT1.on(events.NewMessage(incoming=True, pattern=r"\%sbspam(?: |$)(.*)" % hl))
@BOT2.on(events.NewMessage(incoming=True, pattern=r"\%sbspam(?: |$)(.*)" % hl))
@BOT3.on(events.NewMessage(incoming=True, pattern=r"\%sbspam(?: |$)(.*)" % hl))
@BOT4.on(events.NewMessage(incoming=True, pattern=r"\%sbspam(?: |$)(.*)" % hl))
@BOT5.on(events.NewMessage(incoming=True, pattern=r"\%sbspam(?: |$)(.*)" % hl))
@BOT6.on(events.NewMessage(incoming=True, pattern=r"\%sbspam(?: |$)(.*)" % hl))
@BOT7.on(events.NewMessage(incoming=True, pattern=r"\%sbspam(?: |$)(.*)" % hl))
@BOT8.on(events.NewMessage(incoming=True, pattern=r"\%sbspam(?: |$)(.*)" % hl))
@BOT9.on(events.NewMessage(incoming=True, pattern=r"\%sbspam(?: |$)(.*)" % hl))
async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗕𝗜𝗥𝗧𝗛𝗗𝗔𝗬 𝗦𝗣𝗔𝗠\n\nCommand:\n\n.bspam <count> <Username of User>\n\n.bspam <count> <reply to a User>\n\nCount must be a integer."
    if e.sender_id in SUDOERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage)
        Deadly = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        bitxh = await e.get_reply_message()
        if len(Deadly) == 2:
            user = str(Deadly[1])
            a = await e.client.get_entity(user)
            g = a.id
            if int(g) in DEADLYSPAM:
                text = f"**» ᴄᴀɴɴᴏᴛ ʀᴀɪᴅ ᴏɴ ᴅᴇᴀᴅʟʏ ᴄʀᴇᴀᴛᴏʀ !**"
                await e.reply(text)
            elif int(g) == config.OWNER_ID:
                text = f"**» ɪ  ᴄᴀɴɴᴏᴛ ʀᴀɪᴅ ᴏɴ ᴍʏ ᴏᴡɴᴇʀ  !**"
                await e.reply(text)
            elif int(g) in SUDOERS:
                text = f"ᴄᴀɴɴᴏᴛ ʀᴀɪᴅ ᴏɴ ꜱᴜᴅᴏᴇʀ"
                await e.reply(text)
            else:
                c = a.first_name
                username = f"[{c}](tg://user?id={g})"
                counter = int(Deadly[0])
                for _ in range(counter):
                    reply = random.choice(BRTHSPAM)
                    caption = f"{username} {reply}"
                    async with e.client.action(e.chat_id, "typing"):
                        await e.client.send_message(e.chat_id, caption)
                        await asyncio.sleep(0.5)
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            if int(g) in DEADLYSPAM:
                text = f"**» ᴄᴀɴɴᴏᴛ ʀᴀɪᴅ ᴏɴ ᴅᴇᴀᴅʟʏ ᴄʀᴇᴀᴛᴏʀ !**"
                await e.reply(text)
            elif int(g) == config.OWNER_ID:
                text = f"**» ɪ  ᴄᴀɴɴᴏᴛ ʀᴀɪᴅ ᴏɴ ᴍʏ ᴏᴡɴᴇʀ  !**"
                await e.reply(text)
            elif int(g) in SUDOERS:
                text = f"ᴄᴀɴɴᴏᴛ ʀᴀɪᴅ ᴏɴ ꜱᴜᴅᴏᴇʀ"
                await e.reply(text)
            else:
                c = b.first_name
                counter = int(Deadly[0])
                username = f"[{c}](tg://user?id={g})"
                for _ in range(counter):
                    reply = random.choice(BRTHSPAM)
                    caption = f"{username} {reply}"
                    async with e.client.action(e.chat_id, "typing"):
                        await e.client.send_message(e.chat_id, caption)
                        await asyncio.sleep(0.3)
        else:
            await e.reply(usage)
