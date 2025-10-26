# file_downloader_conversation.py

import logging
from telethon import TelegramClient, events
from telethon.tl.types import PeerUser
from datetime import datetime
import os
import zipfile

# -------------------------
# CONFIGURATION
# -------------------------
api_id = 25638378           # Replace with your API ID (int)
api_hash = "a0b10cca67d3ffdaae1b3b8e6845fbd9"  # Replace with your API Hash (str)
session_name = "file_downloader_private"  # session file name (will be saved in your local with this name)

# -------------------------
# SETUP LOGGING
# -------------------------
logging.basicConfig(level=logging.INFO)

# -------------------------
# INITIALIZE TELETHON CLIENT
# -------------------------
client = TelegramClient(session_name, api_id, api_hash)

# -------------------------
# HELPER FUNCTIONS
# -------------------------
def zip_folder(folder_path, zip_name):
    with zipfile.ZipFile(zip_name, 'w') as zf:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                zf.write(os.path.join(root, file), arcname=file)

async def download_files(chat, start_date, end_date, types_filter=None, sender_username=None):
    folder = f'download_{datetime.now().strftime("%Y%m%d_%H%M%S")}'
    os.makedirs(folder, exist_ok=True)

    async for message in client.iter_messages(chat, reverse=True):
        if message.date.date() < start_date or message.date.date() > end_date:
            continue
        if sender_username and getattr(message.from_id, 'user_id', None):
            sender = await client.get_entity(message.from_id.user_id)
            if sender.username != sender_username:
                continue
        if message.media:
            if types_filter and message.media.__class__.__name__.lower() not in types_filter:
                continue
            filename = os.path.join(folder, f'{message.id}_{getattr(message.file, "name", "media")}')
            await message.download_media(filename)

    zip_name = folder + '.zip'
    zip_folder(folder, zip_name)
    return zip_name

# -------------------------
# EVENTS
# -------------------------
@client.on(events.NewMessage(pattern='/start'))
async def start_handler(event):
    async with client.conversation(event.chat_id) as conv:
        await conv.send_message("Welcome to Telethon File Downloader!\nPlease enter the target chat username or ID:")
        chat_msg = await conv.get_response()
        chat = chat_msg.text.strip()

        await conv.send_message("Enter start date (YYYY-MM-DD):")
        start_msg = await conv.get_response()
        start_date = datetime.strptime(start_msg.text.strip(), '%Y-%m-%d').date()

        await conv.send_message("Enter end date (YYYY-MM-DD):")
        end_msg = await conv.get_response()
        end_date = datetime.strptime(end_msg.text.strip(), '%Y-%m-%d').date()

        await conv.send_message("Enter media types to download separated by comma (photo,video,document,audio,voice) or 'all':")
        types_msg = await conv.get_response()
        types_input = types_msg.text.strip().lower()
        types_filter = None if types_input == 'all' else [t.strip() for t in types_input.split(',')]

        await conv.send_message("Enter sender username to filter or leave blank for all:")
        sender_msg = await conv.get_response()
        sender_username = sender_msg.text.strip() or None

        await conv.send_message("Downloading files, please wait...")
        zip_file = await download_files(chat, start_date, end_date, types_filter, sender_username)

        await conv.send_message(f"Download complete! Here is your ZIP: {zip_file}")

# -------------------------
# RUN CLIENT
# -------------------------
print("Starting Telethon File Downloader (private flow)...")
client.start()
client.run_until_disconnected()
