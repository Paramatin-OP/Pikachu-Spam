import os
from telethon import events, Button, custom
from Pikachu.config import Config

from Pikachu import ALIVE_NAME, bot 

currentversion = "2.1"


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "PikaChuu.."
ASSIS_PIC = os.environ.get("ASSIS_PIC", None)
if ASSIS_PIC is None:
     PM_IMG = "https://te.legra.ph/file/31eb96e606a52078e7406.mp4"
else:
     PM_IMG = ASSIS_PIC


pm_caption = "»»» ʜᴇᴇʟʟʟʟᴏᴏᴏ ᴊɪɪ...👻\n»»» ᴍᴇ ᴘɪᴋᴀᴄʜᴜ..😁 [ᴊᴀss ʙʜᴀɪʏᴀ](https://t.me/Its_JassManak) ᴋᴀ ᴘᴇʀsᴏɴᴀʟ sᴘᴀᴍ ʙᴏᴛ..🤡\n ᴋᴜᴄʜ ʜᴇʟᴘ ᴄʜᴀʜɪʏᴇ ᴛᴏ [ᴊᴀss ʙʜᴀɪʏᴀ](https://t.me/Its_JassManak) ᴋᴏ ᴘᴜᴄʜ ʟᴏ..👑
@tgbot.on(events.NewMessage(pattern="^/alive" , func=lambda e: e.sender_id == bot.uid))
async def _(event):
    await tgbot.send_file(event.chat_id, PM_IMG, caption=pm_caption, buttons=light) 
