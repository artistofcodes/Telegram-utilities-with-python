# Telegram Utilities with Python  

A collection of simple and useful Python scripts to make working with **Telegram Bots** easier.From fetching chat IDs to broadcasting messages and automating common bot tasks.  

---

## 🧰 Repository Structure  

```
telegram-utilities-with-python/
│
├── chat_id_fetcher/
│   └── chat_id_fetcher.py
│
├── message_broadcaster/
│   └── broadcast.py
│
└── README.md
```

---

## 📜 Features  

### 1. Chat ID Fetcher
Fetches the chat ID of a user or group where the bot is added.  
Helpful when you need the `chat_id` to send messages or automate replies.  

**Usage:**
1. Replace your bot token in the code.  
2. Run the script.  
3. Send any message to your bot or group and the terminal will display the chat ID.  

**Example:**
```bash
python chat_id_fetcher.py
```

---

### 2. Message Broadcaster
Sends a message to multiple chat IDs at once.Useful for broadcasting announcements or automated alerts.  

**Usage:**
1. Replace `YOUR_BOT_TOKEN_HERE` with your bot token.  
2. Add chat IDs in the list.  
3. Edit the message text.  
4. Run the script.  

**Example:**
```bash
python broadcast.py
```

---

## ⚙️ Requirements  

- Python 3.7+  
- `requests` library  

Install dependencies:  
```bash
pip install requests
```

---

## 🚀 Future Additions  

- Group member counter  
- User info fetcher  
- File downloader/forwarder  
- Bot command menu setup  

---

## 🧑‍💻 Contributing  
Pull requests are welcome!  
If you have other handy Telegram bot utilities, feel free to add them to the repo.  

---

## 📄 License  
This project is licensed under the **MIT License**.free to use and modify.  

---
