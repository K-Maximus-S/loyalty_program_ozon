from django.db import models


class User_tg(models.Model):
    user_id = models.CharField(max_length=50, unique=True, verbose_name='id пользователя')
    user_name = models.CharField(max_length=128, unique=True, verbose_name='name пользователя')

    def __str__(self):
        return f'user_id: {self.user_id} | user_name: {self.user_name}'

class Deportment_worker_ozon(models.Model):
    role = models.TextField(verbose_name='Роль')
    work_with_user = models.TextField(verbose_name='Доступ к общению с клиентом')

    def __str__(self):
        return f'Роль: {self.role} | Доступ к общению с клиентом: {self.work_with_user}'


class User_worker_ozon(models.Model):
    user_id = models.CharField(max_length=50, unique=True, verbose_name='id ТГ работника')
    user_name = models.CharField(max_length=128, unique=True, verbose_name='name ТГ работника')
    role = models.ForeignKey(to=Deportment_worker_ozon, on_delete=models.CASCADE, verbose_name='Роль')
    access = models.TextField(null=True, blank=True, verbose_name='Активация пользователя')  # TODO: обязательную активацию нужно будет сделать

    def __str__(self):
        return f'id ТГ работника: {self.user_id} | name ТГ работника: {self.user_name} | {self.role} | Активация пользователя: {self.access}'


class Marketing(models.Model):
    title = models.TextField(verbose_name='Название акции/предложения')
    description = models.TextField(verbose_name='Описание акции/предложения')
    functions = models.TextField(null=True, blank=True, verbose_name='Функции акции/предложения (подарок,баллы, итд')
    image = models.ImageField(null=True, blank=True, upload_to='marketing_images')

    def __str__(self):
        return f'Название акции/предложения: {self.title}'


class Emoji(models.Model):
    title = models.TextField(verbose_name='Название эмодзи')
    image = models.ImageField(upload_to='emoji_images')

    def __str__(self):
        return f'Название эмодзи: {self.title}'

class Question_answer(models.Model):
    title = models.TextField(verbose_name='Название вопроса')
    description = models.TextField(verbose_name='Описание вопроса')
    link = models.TextField(null=True, blank=True, verbose_name='Ссылка на источник')
    image = models.ImageField(null=True, blank=True, upload_to='question_answer_images')

    def __str__(self):
        return f'Название вопроса: {self.title}'

class Question_user(models.Model):
    user_id = models.ForeignKey(to=User_tg, on_delete=models.CASCADE, verbose_name='Пользователь')
    raw_text = models.TextField(verbose_name='Описание вопроса')
    manager_id = models.ForeignKey(to=User_worker_ozon, on_delete=models.CASCADE, verbose_name='Назначенный менеджер')
    manager_logic = models.CharField(max_length=50, unique=True, verbose_name='Результат ответа менеджера и закрытие вопроса')
    manager_text = models.TextField(null=True, blank=True, verbose_name='Описание ответа менеджера')

    def __str__(self):
        return f'Пользователь: {self.user_id} | Результат ответа менеджера и закрытие вопроса: {self.manager_logic}'

class Query_log(models.Model):
    data_time = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время')
    raw_text = models.TextField(verbose_name='Текс/данные запроса')

    def __str__(self):
        return f'Дата и время запроса: {self.data_time}'


