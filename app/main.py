from fastapi import FastAPI
from app.config import settings
from app.notifiers.telegram import TelegramNotifier

notifier = TelegramNotifier(token=settings.telegram_bot_token)

app = FastAPI()


@app.get("/health")
def check_health():
    return {"status":"ok"}

@app.get("/test-notifier")
async def test_notifier():
    await notifier.send(chat_id=settings.telegram_chat_id,text="Hello Sir!! Daily news Here.....")

    return {"status":"sent"}