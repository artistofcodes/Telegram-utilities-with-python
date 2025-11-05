# Telegram-utilities-with-python

A growing collection of practical Telegram automation utilities built using Python.  
Includes bot helpers, automation scripts, chat exporting, media downloading, message broadcasting, and more.

> Updated regularly with fresh ideas and daily utilities!

---

## ⭐ Features

- Multiple Telegram automation utilities in one repo
- Supports **Telethon** and **python-telegram-bot**
- Easy to set up and run
- Well-structured utilities with clear purpose
- Beginner-friendly scripts for Telegram developers
- MIT Licensed — free to use and contribute

---

## 🛠️ Requirements

- Python **3.8+**
- Telegram API credentials  
  (API ID & API Hash from https://my.telegram.org/auth)

---

## 📦 Installation

```bash
git clone https://github.com/artistofcodes/Telegram-utilities-with-python.git
cd Telegram-utilities-with-python
pip install -r requirements.txt
```

---

## ⚙️ Libraries Used

| Library | Purpose |
|--------|---------|
| Telethon | User account automation & chat utilities |
| python-telegram-bot | Bot automation utilities |

### Install Telethon
```bash
pip install telethon
```

### Install python-telegram-bot
```bash
pip install python-telegram-bot
```

---

## 📁 Repo Structure (Example Layout)

```
Telegram-utilities-with-python/
 ├─ telethon/
 │   ├─ chat_id_fetcher.py
 │   ├─ message_auto_reply.py
 │   └─ ...
 ├─ bot/
 │   ├─ simple_reply_bot.py
 │   ├─ file_forwarder_bot.py
 │   └─ ...
 ├─ utils/
 │   └─ helper_functions.py
 ├─ README.md
 └─ requirements.txt
```

---

## ✅ Utilities List

| Sl.No | Script | Type | Description |
|------|--------|------|-------------|
| 1 | chat_id_fetcher.py | Telethon | Fetch chat ID for user/group/channel |
| 2 | file_downloader.py | Telethon | Download media/files from any chat |
| 3 | broadcast_message.py | python-telegram-bot | Broadcast message to pre-defined users |
| 4 | auto_forward_bot.py (coming soon) | Bot | Forward messages between chats |
| 5 | google_drive_uploader.py (coming soon) | Telethon | Auto-upload media to Google Drive |
| 6 | spam_control_bot.py (coming soon) | Bot | Prevent spam in groups with rules |

> More utilities are added frequently.Stay tuned!

---

## ▶️ Usage

Each script contains setup instructions in comments.  
Example:

```bash
python telethon/chat_id_fetcher.py
```

Add your:
- API ID
- API Hash
- Bot Token (for bot utilities)
- Target chat details

---

## 🚀 Roadmap

- Add **GUI app** using Python + Qt/CustomTkinter
- Add **auto-backup chat exporter**
- Add **YouTube -> Telegram media tools**
- Create **Docker support** for easy deployment
- Add **logging + error handling features**

---

## 🤝 Contributing

Contributions are always welcome!

To contribute:
1. Fork the repo
2. Create a branch (`feature-new-utility`)
3. Add your script in proper folder
4. Submit a pull request

Please follow:
- Clean, well-commented code
- Short README section for every new utility
- Use a descriptive file name

---

## 📜 License

This project is licensed under the **MIT License** — free for personal & commercial use.

---

## ⭐ Show Your Support

If this repo helped you:

✅ Give it a **Star** on GitHub  
✅ Share with other Telegram developers  
✅ Contribute your own utilities!

---

### Made with Python by `artistofcodes`
