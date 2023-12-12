from bot.markup.markup import Keyboards
from db.db_work import DBManager
from bot.verification.user_verification import Verification
from marketing import Marketing


class Handler:

    def __init__(self, bot):
        # получаем объект бота
        self.bot = bot
        # инициализируем разметку кнопок
        self.keybords = Keyboards()
        # инициализируем менеджер для работы с БД
        self.BD = DBManager()
        # инициализируем идентификации
        self.verification = Verification()
        # инициализируем файл маркетинга
        self.marketing = Marketing()


    def handle(self):
        pass