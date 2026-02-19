import os
import telebot # مكتبة أسهل وأسرع للرد الفوري

# سحب التوكن من Railway
BOT_TOKEN = os.getenv("BOT_TOKEN")
SERVER_URL = "https://simba-stream-server-production.up.railway.app"

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(content_types=['video', 'document'])
def send_link(message):
    # الحصول على الـ File ID
    file_id = message.video.file_id if message.video else message.document.file_id
    
    # تكوين الرابط المباشر
    direct_link = f"{SERVER_URL}/stream/{file_id}"
    
    # الرد المباشر عليك
    bot.reply_to(message, f"✅ أبشر يا أحمد.. هذا رابط فيلمك المباشر:\n\n{direct_link}")

if __name__ == "__main__":
    print("البوت شغال هسة يا بطل...")
    bot.infinity_polling()
