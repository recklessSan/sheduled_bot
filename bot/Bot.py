from telegram.ext import Updater
from bot.handlers import Handlers
from telegram.ext import MessageHandler, Filters
from db.api import DB


class Bot:
    def __init__(self, bot):
        db = DB()
        settings = db.select_key(bot)
        token = settings.token
        self.updater = Updater(token=token, use_context=True)
        message_handler = MessageHandler(Filters.text, Handlers.test)
        self.updater.dispatcher.add_handler(message_handler)

    def start(self):
        self.updater.start_polling()
