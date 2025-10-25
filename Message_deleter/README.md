# Telegram Message Deleter

A simple Python utility to **delete Telegram messages** (single or bulk) using the Telegram Bot API.

---

## 🚀 Features
- Delete a **single message** by ID.
- Delete **multiple messages** in a range.
- Works for **private chats or groups** where the bot is an admin.

---

## 🧠 Prerequisites
- Python 3.8+
- Install dependencies:
  ```bash
  pip install python-telegram-bot
  ```

- Create a Telegram bot via [@BotFather](https://t.me/BotFather)
- Get your **bot token** and **chat ID**

---

## ⚙️ Usage
1. Update your bot token and chat ID inside `message_deleter.py`:
   ```python
   BOT_TOKEN = "YOUR_BOT_TOKEN"
   CHAT_ID = "YOUR_CHAT_ID"
   ```
2. Run the script:
   ```bash
   python message_deleter.py
   ```
3. Choose an option:
   - `1` → Delete a specific message by ID  
   - `2` → Delete messages within a range  

---

## ⚠️ Note
- The bot must have **admin permissions** in the group to delete messages.  
- Telegram only allows deleting messages **less than 48 hours old**.

---

## 📄 License
Licensed under the [MIT License](../LICENSE)
