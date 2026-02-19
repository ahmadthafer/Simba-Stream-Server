import os
import logging
from pyrogram import Client, filters

# سيقوم الكود الآن بسحب المعلومات تلقائياً من Railway Variables
API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
# تأكد أن هذا الرابط هو رابط سيرفرك الصحيح
SERVER_URL = "https://simba-stream-server-production.up.railway.app"

app = Client("simba_bot", api_id=int(API_ID), api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.video | filters.document)
async def send_link(client, message):
    file_id = message.video.file_id if message.video else message.document.file_id
    # هذا هو السطر اللي راح يعطيك الرابط المباشر
    direct_link = f"{SERVER_URL}/stream/{file_id}"
    await message.reply_text(f"✅ أبشر يا أحمد.. هذا رابط فيلمك المباشر:\n\n`{direct_link}`")

if __name__ == "__main__":
    app.run()
