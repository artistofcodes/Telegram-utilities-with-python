import requests

# Replace with your bot token
BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"

# List of chat IDs (users or groups)
chat_ids = [123,456,789] #use your chat IDs here.

# Message to broadcast
message = "Hello! This is a test broadcast from my Telegram bot."

def send_message(chat_id, text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": chat_id, "text": text}
    requests.post(url, data=payload)

for chat_id in chat_ids: #sending message
    send_message(chat_id, message)
    print(f"Message sent to {chat_id}")
