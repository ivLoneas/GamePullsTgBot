from src.config import ALERTS_DAYS
from src.model.polls.PlayTimePoll import PlayTimePoll

playTimePolls = [PlayTimePoll(day) for day in ALERTS_DAYS]
