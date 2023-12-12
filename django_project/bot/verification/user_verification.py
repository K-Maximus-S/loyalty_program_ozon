from db.db_work import DBManager


class Users_DB_result:
    """Структура user из БД User_tg"""
    def __init__(self, user_id, user_name):
        self.user_id = user_id
        self.user_name = user_name

class Verification:
    """Класс идентификации"""

    def __init__(self):
        self.BD = DBManager()

        self.list_users = []

    # Возвращает список пользователей из БД
    def select_users_DB_User_tg(self):
        """Возвращает список пользователей из БД"""
        # Получаем результат из БД таблицы
        self.list_users.clear()
        db_users_tgs = self.BD.select_db_user_tg()
        # Проходимся по списку
        for user_tg in db_users_tgs:
            user_id = user_tg.user_id
            user_name = user_tg.user_name

            # Заносим в шаблон
            user_object = Users_DB_result(
                user_id=user_id,
                user_name=user_name
            )
            self.list_users.append(user_object)
            # TODO: return почему не использую?

    # Проверка пользователя на идентификации 2 параметрам
    def user_verification(self, update):
        """
            Проверяем пользователя:
                1) user_id -, user_name -
                2) user_id +, user_name +
        """
        user_result = None

        self.select_users_DB_User_tg()

        for user in self.list_users:
            user_id = user.user_id
            user_name = user.user_name
            if user_id == str(update.message.from_user.id) and user_name == update.message.from_user.name:
                user_result = 'True'
                break
            else:
                user_result = 'False'
        return user_result