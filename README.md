# Utilities with Python  

A collection of Python scripts for automating Telegram and other everyday tasks using powerful libraries like **Telethon** and **PyDrive2**.  
Each utility is self-contained and includes a setup guide for easy use.

---

## 📚 Table of Contents
1. [Overview](#-utilities-with-python)
2. [Telethon File Downloader (Private Chat Flow)](#1-telethon-file-downloader-private-chat-flow)
3. [Telegram → Google Drive Chat Backup](#2-telegram--google-drive-chat-backup)
4. [Coming Soon](#-coming-soon)
5. [License](#license)

---

![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Telethon](https://img.shields.io/badge/Telethon-latest-orange)
![PyDrive2](https://img.shields.io/badge/PyDrive2-enabled-yellow)

---

## 1. Telethon File Downloader (Private Chat Flow)  
A Telethon script that runs as a user client and interacts with you via **private messages** to download media from any chat.

**Features:**  
- Works through private chat commands (`/start`)  
- Specify target chat (username or ID)  
- Supports date range filtering (`YYYY-MM-DD`)  
- File type filters (`photo`, `video`, `document`, `audio`, `voice`, `all`)  
- Optional sender username filter  
- Creates a ZIP of downloaded files and sends it back to you  
- Fully interactive chat flow  

**Setup:**  
1. Create a Telegram app at [https://my.telegram.org](https://my.telegram.org)  
2. Note your `api_id` and `api_hash`  
3. Install dependencies:
   ```bash
   pip install telethon
   ```
   If VS Code shows  
   `Import "telethon.errors" could not be resolved`,  
   install the library and select the right Python interpreter (`Ctrl + Shift + P → Python: Select Interpreter`).  
4. Run the script:
   ```bash
   python file_downloader.py
   ```
5. Sign in once with your phone number — a `.session` file will be created automatically.

**Limitations:**  
- Works only for user accounts (not bots)  
- Requires you to be a member of the target chat  
- Avoid downloading private content without consent  

---

## 2. Telegram → Google Drive Chat Backup  
A script that connects your Telegram account and automatically backs up chat media to **Google Drive**.

**Features:**  
- Backs up files from Telegram chats directly to Google Drive  
- Works with your user account (not bot)  
- Creates a Drive folder named after the chat  
- Uses `Telethon` + `PyDrive2`  
- Resumable uploads and date-based filtering  

**Setup:**  
1. Create a Telegram app at [https://my.telegram.org](https://my.telegram.org)  
   → get `api_id` and `api_hash`  
2. Create a **Google Cloud Project** and enable the **Drive API**  
3. Download `client_secrets.json` and place it in the script directory  
4. Install dependencies:
   ```bash
   pip install telethon pydrive2
   ```
5. Run the script:
   ```bash
   python tg_drive_backup.py
   ```
6. On the first run, it will open a browser for Google Drive authorization.  
   Once completed, your Telegram chat media will upload automatically.

**Optional Extensions:**  
- Scheduled daily backups  
- Folder-wise Drive organization  
- Automatic compression before upload  

---

## 🧩 Coming Soon  
- Telegram channel analytics  
- Auto-forwarder with filters  
- Scheduled message sender  

---

## License  
MIT License © 2025  
