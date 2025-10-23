#Use this code to get the chat_id or Group_if of telegram where you want to use your Telegram Bot

import requests
import time

TELEGRAM_BOT_TOKEN = "YOUR BOT TOKEN"

def get_updates(offset=None):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/getUpdates"
    params = {"timeout": 100, "offset": offset}
    response = requests.get(url, params=params)
    return response.json()

def main():
    offset = None
    print("Send a message in your Telegram group to the bot, then wait...")
    while True:
        updates = get_updates(offset)
        if updates and updates.get("result"):
            for update in updates["result"]:
                offset = update["update_id"] + 1
                if "message" in update:
                    chat = update["message"]["chat"]
                    print(f"Chat Title: {chat.get('title')}")  # Group name if group chat
                    print(f"Chat ID: {chat.get('id')}")
                    return
        time.sleep(1)

if __name__ == "__main__":
    main()
