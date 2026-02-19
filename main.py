import os
import telebot

# سحب التوكن من Variables في Railway
BOT_TOKEN = os.getenv("BOT_TOKEN")
# رابط سيرفرك اللي شغال هسة
SERVER_URL = "https://simba-stream-server-production.up.railway.app"

bot = telebot.TeleBot(BOT_TOKEN)

# التعامل مع الفيديوهات والملفات لرد الرابط فوراً
@bot.message_handler(content_types=['video', 'document'])
def send_direct_link(message):
    try:
        # استخراج الـ File ID
        file_id = message.video.file_id if message.video else message.document.file_id
        
        # تكوين الرابط المباشر
        direct_link = f"{SERVER_URL}/stream/{file_id}"
        
        # الرد المباشر على الرسالة
        bot.reply_to(message, f"✅ تم استلام الفيلم يا أحمد!\n\nرابط البث المباشر:\n`{direct_link}`")
        print(f"تم إرسال رابط للملف: {file_id}")
    except Exception as e:
        bot.reply_to(message, f"❌ حدث خطأ: {e}")

# أمر البداية للتأكد أن البوت صاحي
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "هلا بيك يا أحمد! البوت شغال هسة. حول لي أي فيلم وراح أعطيك الرابط المباشر فوراً.")

if __name__ == "__main__":
    print("البوت بدأ العمل.. بانتظار الأفلام!")
    bot.infinity_polling()
