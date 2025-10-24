# Message Broadcaster  

A simple Python utility that sends a broadcast message to multiple Telegram users or groups using a single bot token.  
Perfect for sending updates, announcements, or alerts to multiple chat IDs at once.  

---

## 🧩 How It Works  

This script uses the Telegram Bot API’s `sendMessage` endpoint to loop through a list of chat IDs and send the same message to each.  

---

## ⚙️ Setup  

### Requirements  
- Python 3.7+  
- `requests` library  

Install dependencies:  
```bash
pip install requests
```

---

## ▶️ Usage  

1. Replace `YOUR_BOT_TOKEN_HERE` with your actual bot token.  
2. Add your user or group chat IDs to the `chat_ids` list.  
3. Customize your message text.  
4. Run the script:  

```bash
python broadcast.py
```

Each chat ID in the list will receive the message automatically.  

---

## 💡 Notes  

- Works for both **private users** and **groups** (use negative IDs for groups).  
- The bot must be added to each group before sending messages.  
- To get chat IDs, use the **Chat ID Fetcher** utility from this repository.  

---

## 📄 License  
This project is licensed under the **MIT License** — free to use and modify.  
