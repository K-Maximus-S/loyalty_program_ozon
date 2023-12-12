from telegram.ext import CommandHandler
from bot.bot_work.handler import Handler
from bot.massage import MESSAGES
import time


class HandlerCommands(Handler):
    """
    Класс обрабатывает входящие команды /start  и т.п.
    """

    def __init__(self, bot):
        super().__init__(bot)

    def start(self, update, context):
        """
        Обрабатывает входящие /start команды.
        """
        verification_result = self.verification.user_verification(update)
        if verification_result == 'True':
            update.message.reply_text(text=MESSAGES['greeting_old'], parse_mode="HTML",
                                      reply_markup=self.keybords.start_menu())
        elif verification_result == 'False':
            self.BD.insert_db_user_tg(
                user_id=update.message.from_user.id,
                user_name=update.message.from_user.name,
            )
            update.message.reply_text(text=MESSAGES['greeting_new'], parse_mode="HTML",
                                      reply_markup=self.keybords.start_menu_marketing())
    def handle(self):
        self.bot.add_handler(CommandHandler('start', self.start))
