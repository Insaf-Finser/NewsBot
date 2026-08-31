from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parent.parent))
from app.config import settings
from app.notifiers.telegram import TelegramNotifier
import asyncio

async def send_test_message():
    tel = TelegramNotifier(token=settings.telegram_bot_token)
    await tel.send(chat_id=settings.telegram_chat_id,text="Hello Boss")


if __name__ == "__main__":
    asyncio.run(send_test_message())

