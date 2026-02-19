import os
from pyrogram import Client
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import uvicorn

# جلب المعلومات من إعدادات Railway
API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

app = FastAPI()
bot = Client("SimbaStream", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_event("startup")
async def startup():
    # تشغيل البوت عند بدء السيرفر
    await bot.start()

@app.get("/")
async def root():
    return {"status": "Simba Stream Server is Online!"}

@app.get("/stream/{file_id}")
async def stream_video(file_id: str):
    # هذه الدالة تقوم بسحب الميديا وتمريرها مباشرة بدون خزنها في السيرفر
    async def file_generator():
        async for chunk in bot.stream_media(file_id):
            yield chunk
    return StreamingResponse(file_generator(), media_type="video/mp4")

if __name__ == "__main__":
    # تحديد المنفذ تلقائياً ليتناسب مع Railway
    port = int(os.environ.get("PORT", 8080))
    uvicorn.run(app, host="0.0.0.0", port=port)