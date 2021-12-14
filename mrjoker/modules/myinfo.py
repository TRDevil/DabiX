from telethon import events, Button, custom, version
from telethon.tl.types import ChannelParticipantsAdmins
import asyncio
import os,re
import requests
import datetime
import time
from datetime import datetime
import random
from PIL import Image
from io import BytesIO
from mrjoker import telethn as bot
from mrjoker import telethn as tgbot
from mrjoker.events import register
from mrjoker import dispatcher


edit_time = 5
""" =======================CONSTANTS====================== """
file1 = "https://telegra.ph/file/afd9a70da1805f432c395.jpg"
file2 = "https://telegra.ph/file/1f6120f20477589316652.jpg"
file3 = "https://telegra.ph/file/241928efae7a97ed33498.jpg"
file4 = "https://telegra.ph/file/c12e1078e8b5337b03053.jpg"
file5 = "https://telegra.ph/file/96d2c937c6a31813627c2.jpg"
""" =======================CONSTANTS====================== """

@register(pattern="/dabixinfo")
async def proboyx(event):
    chat = await event.get_chat()
    current_time = datetime.utcnow()
    betsy = event.sender.first_name
    button = [[custom.Button.inline("✉ Click Me",data="information")]]
    on = await bot.send_file(event.chat_id, file=file2,caption= f"➣ Hey {betsy}, I'm DabiX\n➣ I'm Connected In [𐒨яσω∂χѕтяιкє](t.me/CrowdXStrike)\n➣ Click The Button Below To Get Your Info! In [★彡  𐒨χS ∂в 彡★](t.me/CrowdXStrikeLogs) ", buttons=button)

    await asyncio.sleep(edit_time)
    ok = await bot.edit_message(event.chat_id, on, file=file3, buttons=button) 

    await asyncio.sleep(edit_time)
    ok2 = await bot.edit_message(event.chat_id, ok, file=file5, buttons=button)

    await asyncio.sleep(edit_time)
    ok3 = await bot.edit_message(event.chat_id, ok2, file=file1, buttons=button)

    await asyncio.sleep(edit_time)
    ok7 = await bot.edit_message(event.chat_id, ok6, file=file4, buttons=button)
    
    await asyncio.sleep(edit_time)
    ok4 = await bot.edit_message(event.chat_id, ok3, file=file2, buttons=button)
    
    await asyncio.sleep(edit_time)
    ok5 = await bot.edit_message(event.chat_id, ok4, file=file1, buttons=button)
    
    await asyncio.sleep(edit_time)
    ok6 = await bot.edit_message(event.chat_id, ok5, file=file3, buttons=button)
    
    await asyncio.sleep(edit_time)
    ok7 = await bot.edit_message(event.chat_id, ok6, file=file5, buttons=button)

    await asyncio.sleep(edit_time)
    ok7 = await bot.edit_message(event.chat_id, ok6, file=file4, buttons=button)

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"information")))
async def callback_query_handler(event):
  try:
    boy = event.sender_id
    PRO = await bot.get_entity(boy)
    LILIE = "╚»★ уσυя ∂єтαιℓѕ ιи 𐒨χѕ ∂в ★«╝ \n\n"
    LILIE += f"➣ғɪʀsᴛ ɴᴀᴍᴇ : {PRO.first_name} \n"
    LILIE += f"➣ʟᴀsᴛ ɴᴀᴍᴇ : {PRO.last_name}\n"
    LILIE += f"➣ʏᴏᴜ ᴀʀᴇ ʙᴏᴛ : {PRO.bot} \n"
    LILIE += f"➣ʀᴇsᴛʀɪᴄᴛᴇᴅ ᴜsᴇʀ : {PRO.restricted} \n"
    LILIE += f"➣ʏᴏᴜʀ ɪᴅ : {boy}\n"
    LILIE += f"➣ʏᴏᴜʀ ᴜsᴇʀɴᴀᴍᴇ : {PRO.username}\n"
    await event.answer(LILIE, alert=True)
  except Exception as e:
    await event.reply(f"{e}")

__help__ = """
/dabixinfo: Shows Your Info In Inline Screen
"""

__mod_name__ = "DabiXInfo"
__command_list__ = [
    "myinfo"
]
