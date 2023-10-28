from src.config import ALERTS_DAYS, SESSION_TIMES
from src.model.Bot import Bot
from src.controllers.BotController import BotController

gameAlertBot = Bot()
gameAlertBot.days_of_game_sessions = ALERTS_DAYS
gameAlertBot.session_times = SESSION_TIMES

controller = BotController(gameAlertBot)
controller.run_in_debug()

print("run")
gameAlertBot.run()
