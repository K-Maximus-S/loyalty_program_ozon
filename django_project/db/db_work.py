from db.models import User_tg, Deportment_worker_ozon, User_worker_ozon, Marketing, Emoji, Question_answer, Question_user, Query_log


class DBManager:
    """Класс менеджер для работы с БД"""

    # Получаем результат из БД таблицы User_tg
    def select_db_user_tg(self):
        """Получаем результат из БД таблицы User_tg"""
        result = User_tg.objects.all() # TODO: ?
        return result

    # Добавление пользователя в БД таблицы User_tg
    def insert_db_user_tg(self, user_id, user_name):
        """Добавление пользователя в БД таблицы User_tg"""
        result = User_tg.objects.create(
                                        user_id=user_id,
                                        user_name=user_name
                                        )
        return