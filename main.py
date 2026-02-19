# كود تحديث البوت ليرسل روابط مباشرة
import logging
from pyrogram import Client, filters

# الإعدادات (سيأخذها من Variables في Railway)
API_ID = "ضع_هنا_API_ID"
API_HASH = "ضع_هنا_API_HASH"
BOT_TOKEN = "8259074887:AAEqseosPRLXkzUQ5Vqc67FBsmT5MpbU9hw"
SERVER_URL = "https://simba-stream-server-production.up.railway.app"

app = Client("simba_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.video | filters.document)
async def send_link(client, message):
    file_id = message.video.file_id if message.video else message.document.file_id
    direct_link = f"{SERVER_URL}/stream/{file_id}"
    await message.reply_text(f"✅ تم توليد الرابط المباشر لفيلمك:\n\n`{direct_link}`")

app.run()
