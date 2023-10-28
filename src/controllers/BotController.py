import telebot.types

from src.messages import MESSAGES
from src.model.Bot import Bot
from src.model.SingletonMeta import SingletonMeta
from src.model.polls.polls import playTimePolls


class BotController(metaclass=SingletonMeta):
    def __init__(self, bot):
        self.bot: Bot = bot
        self._telebot = bot.bot

    def welcome(self):
        @self._telebot.message_handler(commands=['help', 'start'])
        def send_welcome(message: telebot.types.Message):
            self._telebot.reply_to(message, MESSAGES["welcome"].format(BotController.author_full_name(message)))

    def send_all_polls(self):
        @self._telebot.message_handler(commands=['all_polls'])
        def sel_all_polls(message: telebot.types.Message):
            for poll in playTimePolls:
                self._telebot.send_poll(message.chat.id, question=poll.question,
                                        options=poll.options, is_anonymous=poll.is_anonymous,
                                        allows_multiple_answers=poll.allow_multiple_choice)

    def echo(self):
        @self._telebot.message_handler(func=lambda message: True)
        def echo_message(message: telebot.types.Message):
            self._telebot.reply_to(message, message.text)

    def run_in_debug(self):
        self.welcome()
        self.send_all_polls()
        self.echo()

    @staticmethod
    def author_full_name(message: telebot.types.Message) -> str:
        return f"{message.from_user.first_name} {message.from_user.last_name}"
