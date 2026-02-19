import os
from pyrogram import Client, filters

# سحب المعلومات من Railway Variables
API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
SERVER_URL = "https://simba-stream-server-production.up.railway.app"

app = Client("simba_bot", api_id=int(API_ID), api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.video | filters.document)
async def send_link(client, message):
    # الحصول على الـ File ID باستخدام Pyrogram
    file_id = message.video.file_id if message.video else message.document.file_id
    direct_link = f"{SERVER_URL}/stream/{file_id}"
    
    await message.reply_text(f"✅ تم استلام الفيلم!\n\nرابط البث المباشر:\n`{direct_link}`")

if __name__ == "__main__":
    app.run()
