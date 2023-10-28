from src.config import SESSION_TIMES
from src.messages import MESSAGES
from src.model.polls.Poll import Poll
from src.utils import next_week_day


class PlayTimePoll(Poll):
    def __init__(self, day: str):
        day_of_poll = day
        day_of_play = next_week_day(day)
        super().__init__(MESSAGES["play_time_poll_question"].format(day_of_play), SESSION_TIMES, True, False)
