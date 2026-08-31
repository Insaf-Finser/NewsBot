from telegram import Bot
from app.notifiers.base import Notifier

class TelegramNotifier(Notifier):

    def __init__(self,token:str):
        self.bot = Bot(token=token)
    async def send(self,chat_id:str,text:str) ->None:
        await self.bot.send_message(chat_id=chat_id,text=text)