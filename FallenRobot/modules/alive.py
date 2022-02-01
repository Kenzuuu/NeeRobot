import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from FallenRobot.events import register
from FallenRobot import telethn as tbot


PHOTO = "https://telegra.ph/file/a184ecef81e92a6854859.jpg"

@register(pattern=("/alive"))
async def awake(event):
  TEXT = f"**ʜᴇʏ​ [{event.sender.first_name}](tg://user?id={event.sender.id}),\n\nɪ ᴀᴍ ᴋᴇɴᴢᴜ ʀᴏʙᴏᴛ​.**\n━━━━━━━━━━━━━━━━━━━\n\n"
  TEXT += f"☆ **ᴍʏ ᴅᴇᴠᴇʟᴏᴘᴇʀ​ : [KENZHU](https://t.me/triplenineee)** \n\n"
  TEXT += f"☆ **ʟɪʙʀᴀʀʏ ᴠᴇʀsɪᴏɴ :** `{telever}` \n\n"
  TEXT += f"☆ **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{tlhver}` \n\n"
  TEXT += f"☆ **ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ :** `{pyrover}` \n━━━━━━━━━━━━━━━━━\n\n"
  BUTTON = [[Button.url("ʜᴇʟᴘ​", "https://t.me/Kenzutapibot?start=help"), Button.url("sᴜᴘᴘᴏʀᴛ​", "https://t.me/Kenzusupport")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=TEXT,  buttons=BUTTON)
