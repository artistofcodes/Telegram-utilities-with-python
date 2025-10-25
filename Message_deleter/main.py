import telegram
from telegram.error import TelegramError

# Replace with your bot token
BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"
CHAT_ID = "YOUR_CHAT_ID_HERE"  # Can be a group or user chat ID

bot = telegram.Bot(token=BOT_TOKEN)

def delete_message(message_id):
    """
    Delete a specific message from a Telegram chat.
    """
    try:
        bot.delete_message(chat_id=CHAT_ID, message_id=message_id)
        print(f"✅ Deleted message ID: {message_id}")
    except TelegramError as e:
        print(f"❌ Error deleting message ID {message_id}: {e}")

def delete_range(start_id, end_id):
    """
    Delete a range of messages between two IDs.
    """
    for message_id in range(start_id, end_id + 1):
        delete_message(message_id)

if __name__ == "__main__":
    print("Telegram Message Deleter")
    print("-------------------------")
    print("1️⃣ Delete a single message")
    print("2️⃣ Delete a range of messages")

    choice = input("Enter your choice (1 or 2): ").strip()

    if choice == "1":
        msg_id = int(input("Enter message ID to delete: "))
        delete_message(msg_id)
    elif choice == "2":
        start_id = int(input("Enter start message ID: "))
        end_id = int(input("Enter end message ID: "))
        delete_range(start_id, end_id)
    else:
        print("Invalid choice.")
