# file_downloader_debug.py

import logging
from telethon import TelegramClient, events

# Replace these with your actual API credentials
api_id = 25638378              # YOUR API_ID (int)
api_hash = "a0b10cca67d3ffdaae1b3b8e6845fbd9"  # YOUR_API_HASH (str)
session_name = "file_downloader_private"  # session file name

# Enable debug logging
logging.basicConfig(level=logging.DEBUG)

print("Starting Telethon File Downloader (debug)...")

client = TelegramClient(session_name, api_id, api_hash)

@client.on(events.NewMessage)
async def message_handler(event):
    print("New message received:", event.raw_text)
    # Simple auto-response to confirm receipt
    await event.respond("✅ Message received by Telethon!")

client.start()
client.run_until_disconnected()
