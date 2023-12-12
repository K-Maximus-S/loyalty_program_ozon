from bot.bot_work.handler import Handler
from telegram.ext import MessageHandler, Filters
from bot.massage import MESSAGES
from bot.config import KEYBOARD


class HandlerAllText(Handler):
    """
    Класс обрабатывает входящие текстовые сообщения от нажатия на кнопки
    """

    def __init__(self, bot):
        super().__init__(bot)

    # Обрабатывает входящие текстовые сообщения от нажатия на КНОПКУ: Отдел качества и заботы
    def frequent_questions(self, update, context):
        """ Обрабатывает входящие текстовые сообщения от нажатия на КНОПКУ: Отдел качества и заботы"""
        update.message.reply_text(text=MESSAGES['frequent_questions'], parse_mode="HTML", reply_markup=self.keybords.frequent_questions())

    # Обрабатывает входящие текстовые сообщения от нажатия на КНОПКУ: О проекте
    def menu_info(self, update, context):
        """ Обрабатывает входящие текстовые сообщения от нажатия на КНОПКУ: О проекте"""
        update.message.reply_text(text=MESSAGES['info'], parse_mode="HTML", reply_markup=self.keybords.back_start_menu())

    # Обрабатывает входящие текстовые сообщения от нажатия на КНОПКУ: О ПВЗ
    def menu_pvz(self, update, context):
        """ Обрабатывает входящие текстовые сообщения от нажатия на КНОПКУ: О ПВЗ"""
        update.message.reply_text(text=MESSAGES['pvz'], parse_mode="HTML", reply_markup=self.keybords.back_start_menu())

    # Обрабатывает входящие текстовые сообщения от нажатия на КНОПКУ: Навигация
    def menu_settings(self, update, context):
        """ Обрабатывает входящие текстовые сообщения от нажатия на КНОПКУ: Настройк"""
        update.message.reply_text(text=MESSAGES['settings'], parse_mode="HTML", reply_markup=self.keybords.back_start_menu())

    # Обрабатывает входящие текстовые сообщения от нажатия на КНОПКУ: Гео-сервисы
    def menu_geo_service(self, update, context):
        """ Обрабатывает входящие текстовые сообщения от нажатия на КНОПКУ: Гео-сервисы"""
        update.message.reply_text(text=MESSAGES['geo_service'], parse_mode="HTML", reply_markup=self.keybords.back_start_menu())

    # Обрабатывает входящие текстовые сообщения от нажатия на КНОПКУ: Соц-сети
    def menu_social_networks(self, update, context):
        """ Обрабатывает входящие текстовые сообщения от нажатия на КНОПКУ: Соц-сети"""
        update.message.reply_text(text=MESSAGES['social_networks'], parse_mode="HTML", reply_markup=self.keybords.back_start_menu())

    # Обрабатывает входящие текстовые сообщения от нажатия на КНОПКУ: График работы ПВЗ
    def menu_work_schedule(self, update, context):
        """ Обрабатывает входящие текстовые сообщения от нажатия на КНОПКУ: График работы ПВЗ"""
        update.message.reply_text(text=MESSAGES['work_schedule'], parse_mode="HTML", reply_markup=self.keybords.back_start_menu())

    # Обрабатывает входящие текстовые сообщения от нажатия на КНОПКУ: Адрес ПВЗ
    def menu_address(self, update, context):
        """ Обрабатывает входящие текстовые сообщения от нажатия на КНОПКУ: Адрес ПВЗ"""
        update.message.reply_text(text=MESSAGES['address'], parse_mode="HTML", reply_markup=self.keybords.back_start_menu())
        # update.message.reply_photo(open('media/question_answer_images/Как_добраться_до_ПВЗ_13.png', 'rb'), reply_markup=self.keybords.back_start_menu())

    # Обрабатывает входящие текстовые сообщения от нажатия на КНОПКУ: Задать вопрос менеджеру
    def menu_ask_manager(self, update, context):
        """ Обрабатывает входящие текстовые сообщения от нажатия на КНОПКУ: Задать вопрос менеджеру"""
        update.message.reply_text(text=MESSAGES['ask_manager'], parse_mode="HTML", reply_markup=self.keybords.back_start_menu())

    # Обрабатывает входящие текстовые сообщения от нажатия на КНОПКУ: Программа лояльности
    def menu_loyalty_program(self, update, context):
        """ Обрабатывает входящие текстовые сообщения от нажатия на КНОПКУ: Программа лояльности"""
        update.message.reply_text(text=MESSAGES['loyalty_program'], parse_mode="HTML", reply_markup=self.keybords.back_start_menu())

    # Обрабатывает входящие текстовые сообщения от нажатия на КНОПКУ: Назад (в start menu)
    def back_start_menu(self, update, context):
        """ Обрабатывает входящие текстовые сообщения от нажатия на КНОПКУ: Назад (в start menu)"""
        update.message.reply_text(text=MESSAGES['back_start_menu'], parse_mode="HTML", reply_markup=self.keybords.start_menu())

    # Обрабатывает входящие текстовые сообщения ОШИБКА НАЖАТИЯ КНОПКИ
    def button_error_menu(self, update, context):
        """ Обрабатывает входящие текстовые сообщения от нажатия на КНОПКУ: Назад (в start menu)"""
        update.message.reply_text(text=MESSAGES['button_error'], parse_mode="HTML", reply_markup=self.keybords.start_menu())

    # Обрабатывает входящие текстовые сообщения
    def filters_text(self, update, context):
        """ Обрабатывает входящие текстовые сообщения от нажатия на КНОПКУ: Назад (в start menu)"""
        if update.message.text == 'Отдел заботы и помощи 🙌🏻':
            self.frequent_questions(update, context)
        elif update.message.text == 'О проекте 📽':
            self.menu_info(update, context)
        elif update.message.text == 'О ПВЗ 🏪':
            self.menu_pvz(update, context)
        elif update.message.text == 'Навигация ⚙':
            self.menu_settings(update, context)
        elif update.message.text == 'Оставить отзыв 💙':
            self.menu_geo_service(update, context)
        elif update.message.text == 'В соцсетях 🌐':
            self.menu_social_networks(update, context)
        elif update.message.text == 'Программа лояльности 💎':
            self.menu_loyalty_program(update, context)
        elif update.message.text == 'График работы ПВЗ ⏳':
            self.menu_work_schedule(update, context)
        elif update.message.text == 'Адрес ПВЗ 📌':
            self.menu_address(update, context)
        elif update.message.text == 'Задать вопрос менеджеру 👩🏻‍💻':
            self.menu_ask_manager(update, context)
        elif update.message.text == 'Назад 🔙':
            self.back_start_menu(update, context)
        else:
            self.button_error_menu(update, context)


    def handle(self):
        """
        Обрабатывает входящие текстовые сообщения
        от нажатия кнопок и ввод текста.
        """
        # ============ Обработка команды финансы после start_menu ==========
        self.bot.add_handler(MessageHandler(Filters.text, callback=self.filters_text))