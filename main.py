import os
from pyrogram import Client, filters

# استلام القيم من Railway Variables
API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

app = Client("test_bot", api_id=int(API_ID), api_hash=API_HASH, bot_token=BOT_TOKEN)

# هذا الفلتر سيرد على أي شيء حرفياً (نص، فيديو، تحويل)
@app.on_message(filters.all)
async def test_reply(client, message):
    await message.reply_text("✅ هلا أحمد! البوت نطق والسيرفر شغال 100%")
    print("تم استلام رسالة بنجاح!")

if __name__ == "__main__":
    app.run()
