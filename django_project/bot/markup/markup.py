from telegram import KeyboardButton, ReplyKeyboardMarkup
from bot import config


class Keyboards:
    """
    Класс Keyboards предназначен для создания и разметки интерфейса бота
    """

    def __init__(self):
        self.markup = None

    def set_btn(self, name):
        """
        Создает и возвращает кнопку по входным параметрам
        """
        keyboard_menu = [
            [KeyboardButton(f"{config.KEYBOARD[ist]}") for ist in name]
        ]
        return keyboard_menu

    # Создает разметку кнопок start_menu
    def start_menu(self):
        """Создает разметку кнопок"""
        list_itm = ['QUALITY_AND_CARE_DEPARTMENT',  'LOYALTY_PROGRAM', 'SETTINGS']

        self.markup = ReplyKeyboardMarkup.from_column([(config.KEYBOARD[button]) for button in list_itm], resize_keyboard=True, one_time_keyboard=True) # TODO: selective - нужен??
        return self.markup

    # Создает разметку кнопок частые вопросы
    def frequent_questions(self):
        """Создает разметку кнопок"""
        list_itm = ['INFO', 'PVZ', 'SOCIAL_NETWORKS', 'GEO_SERVICE', 'MENU_WORK_SCHEDULE', 'MENU_ADDRESS', 'MENU_ASK_MANAGER', 'BACK_START_MENU']
        self.markup = ReplyKeyboardMarkup.from_column([(config.KEYBOARD[button]) for button in list_itm], resize_keyboard=True, one_time_keyboard=True) # TODO: selective - нужен??
        return self.markup

    # Создает разметку кнопки вернуться НАЗАД в start_menu
    def back_start_menu(self):
        """Создает разметку кнопок"""
        list_itm = ['BACK_START_MENU']
        self.markup = ReplyKeyboardMarkup(keyboard=self.set_btn(list_itm), one_time_keyboard=True, resize_keyboard=True)
        return self.markup

    # Создает разметку кнопок start_menu для маркетинга
    def start_menu_marketing(self):
        """Создает разметку кнопок"""
        list_itm = ['SOCIAL_NETWORKS', 'QUALITY_AND_CARE_DEPARTMENT',  'LOYALTY_PROGRAM', 'SETTINGS']

        self.markup = ReplyKeyboardMarkup.from_column([(config.KEYBOARD[button]) for button in list_itm], resize_keyboard=True, one_time_keyboard=True) # TODO: selective - нужен??
        return self.markup

