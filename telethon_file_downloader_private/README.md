# Telethon File Downloader (Private Chat Flow)

This Telethon script runs as a user client and interacts with you in **private messages**.  
It prompts for the target chat, date range, file types, and optional sender username,  
then downloads matching media and returns a ZIP archive in private chat.

## Features
- Private-chat interaction: start the flow by messaging the script's account with `/start`.
- Specify any target chat by username or ID (e.g., `@channelname` or `-1001234567890`).
- Date range input in `YYYY-MM-DD` format (inclusive).
- File type filters: `photo`, `video`, `document`, `audio`, `voice`, or `all`.
- Optional sender username filter (without `@`).
- Downloads files locally, creates a ZIP, and sends it back to you in private chat.

## Requirements
- Python 3.8+
- Telethon

### Install dependencies
```bash
pip install telethon
```

If you see `Import "telethon.errors" could not be resolved` in VS Code, it simply means Telethon is not installed in your current environment.  
Run the above command, then restart VS Code, and ensure the correct Python interpreter is selected via:  
`Ctrl + Shift + P → Python: Select Interpreter`

## Setup
1. Go to [https://my.telegram.org](https://my.telegram.org) and log in with your Telegram account.
2. Click **API Development Tools** and create a new application.
3. You will get:
   - `api_id` (integer)
   - `api_hash` (string)
4. Edit `file_downloader.py` and set:
```python
api_id = YOUR_API_ID           # Replace with your API ID (int)
api_hash = "YOUR_API_HASH"    # Replace with your API Hash (str)
session_name = "file_downloader_private"  # Name for your local session file
```
5. Run the script:
```bash
python file_downloader.py
```
6. The first run will ask you to sign in with your phone number and (optionally) 2FA password, and will create a session file.

## Notes & Limitations
- This runs as a **user account** (not a bot) and requires the account to be a member of the target chat.
- The script asks fresh inputs every time and does not persist settings between runs.
- Be mindful of privacy and permissions before downloading other users' media.
- Large ranges may take long to process; the script iterates through the chat history and filters messages by date.

## License
MIT