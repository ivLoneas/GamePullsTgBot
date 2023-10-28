from typing import List

import telebot

from src.TOKEN import TOKEN
from src.model.SingletonMeta import SingletonMeta


class Bot(metaclass=SingletonMeta):

    def __init__(self):
        self.days_of_game_sessions: List[str] = []
        self.session_times: List[str] = []

        self.bot = telebot.TeleBot(TOKEN)

    def run(self):
        self.bot.infinity_polling()

    def stop(self):
        self.bot.stop_bot()
