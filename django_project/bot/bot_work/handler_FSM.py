from telegram.ext import ConversationHandler, CommandHandler, MessageHandler, Filters
from bot.bot_work.handler import Handler
from bot.bot_work.handler_all_text import HandlerAllText
from bot.massage import MESSAGES
from bot import config


class HandlerFSM(Handler):
    """
    Класс обрабатывает входящие текстовые сообщения от вода текста по системе FSM (конечный автомат)
    """

    def __init__(self, bot):
        super().__init__(bot)
        self.handler_all_text = HandlerAllText(Handler)