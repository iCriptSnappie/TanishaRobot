from TanishaRobot import pbot as app
from os import environ
from pyrogram import Client, filters
from pyrogram.types import ChatJoinRequest, InlineKeyboardButton, InlineKeyboardMarkup

EVAA = [
    [
        InlineKeyboardButton(text="ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ", url=f"https://t.me/TanishaRobot?startgroup=true"),
    ],
]

# Extract environment variables or provide default values
chat_id_env = environ.get("CHAT_ID")
CHAT_ID = [int(app) for app in chat_id_env.split(",")] if chat_id_env else []

TEXT = environ.get("APPROVED_WELCOME_TEXT", "⬤ ʜᴇʟʟᴏ ʙᴀʙʏ ➥ {mention} ♥︎\n\n⬤ ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴛʜᴇ ➥ {title}\n\n")
APPROVED = environ.get("APPROVED_WELCOME", "on").lower()

# Global variable to track the approve status
approve_status = APPROVED == "on"

# Command handler to enable or disable auto approve
@app.on_message(filters.command("joinapproval") & filters.chat(CHAT_ID))
async def toggle_autoapprove(client: app, message):
    global approve_status
    command = message.command
    if len(command) != 2 or command[1] not in ["on", "off"]:
        await message.reply_text("Usage: /joinapproval [on|off]")
        return
    
    if command[1] == "on":
        approve_status = True
        await message.reply_text("Auto-approve has been enabled.")
    else:
        approve_status = False
        await message.reply_text("Auto-approve has been disabled.")

# Define an event handler for chat join requests
@app.on_chat_join_request((filters.group | filters.channel) & filters.chat(CHAT_ID) if CHAT_ID else (filters.group | filters.channel))
async def autoapprove(client: app, message: ChatJoinRequest):
    if not approve_status:
        return  # Exit the function if auto-approve is disabled

    chat = message.chat  # Chat
    user = message.from_user  # User
    print(f"✦ {user.first_name} ᴊᴏɪɴᴇᴅ ♥︎")  # Logs
    await client.approve_chat_join_request(chat_id=chat.id, user_id=user.id)
    if approve_status:
        await client.send_message(
            chat_id=chat.id,
            text=TEXT.format(mention=user.mention, title=chat.title),
            reply_markup=InlineKeyboardMarkup(EVAA),
        )
