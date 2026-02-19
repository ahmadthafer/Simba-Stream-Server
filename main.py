import os
import asyncio
from pyrogram import Client, filters

# استلام القيم من Railway Variables
API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
SERVER_URL = "https://simba-stream-server-production.up.railway.app"

app = Client("simba_bot", api_id=int(API_ID), api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.video | filters.document)
async def send_link(client, message):
    try:
        # استخراج الـ File ID
        file_id = message.video.file_id if message.video else message.document.file_id
        # تكوين الرابط المباشر
        direct_link = f"{SERVER_URL}/stream/{file_id}"
        # الرد على المستخدم
        await message.reply_text(f"✅ تم استلام الفيلم!\n\nرابط البث المباشر لـ Simba:\n`{direct_link}`")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    app.run()
