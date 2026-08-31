from telegram import Bot
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parent.parent))
from app.config import settings
import asyncio


async def send_test_message():
    bot = Bot(token=settings.telegram_bot_token)

    await bot.send_message(chat_id=settings.telegram_chat_id,text="Hello from the Bot")


if __name__ == "__main__":
    asyncio.run(send_test_message())