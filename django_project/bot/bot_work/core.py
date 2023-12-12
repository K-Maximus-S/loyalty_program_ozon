from telegram.ext import Updater
from django_project.settings import TOKEN_TELEGRAM_BOT_API
from bot.bot_work.handler_main import HandlerMain

class TelBot:
    """
    Основной класс телеграмм бота (сервер)
    """

    def __init__(self):
        """
        Инициализация бота
        """
        self.updater = Updater(TOKEN_TELEGRAM_BOT_API)
        self.dp = self.updater.dispatcher
        self.handler = HandlerMain(self.dp)

    def start_handler(self):
        """
        Метод предназначен для старта обработчика событий
        """
        self.handler.handle()

    def run_bot(self):
        """
        Метод запускает основные события сервера
        """
        self.updater.start_polling() # TODO: Переделать. Убрать пулинг
        self.updater.idle()