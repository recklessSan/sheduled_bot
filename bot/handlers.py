import pytz
import re
import logging
from datetime import datetime, timedelta
from db.api import DB
from telegram import ParseMode


db = DB()


class Handlers:
    def __init__(self):
        self.last_list_id = None

    def test(update, context):
        user = update.effective_user.username
        chat_id = update.effective_chat.id
        print(chat_id)
        message = update.effective_message.text
        context.bot.send_message(chat_id, user + '\n' + message)

