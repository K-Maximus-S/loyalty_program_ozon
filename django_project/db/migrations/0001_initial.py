# Generated by Django 4.2 on 2023-11-28 03:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Deportment_worker_ozon",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("role", models.TextField(verbose_name="Роль")),
                (
                    "work_with_user",
                    models.TextField(verbose_name="Доступ к общению с клиентом"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Emoji",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.TextField(verbose_name="Название эмодзи")),
                ("image", models.ImageField(upload_to="emoji_images")),
            ],
        ),
        migrations.CreateModel(
            name="Marketing",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.TextField(verbose_name="Название акции/предложения")),
                (
                    "description",
                    models.TextField(verbose_name="Описание акции/предложения"),
                ),
                (
                    "functions",
                    models.TextField(
                        blank=True,
                        null=True,
                        verbose_name="Функции акции/предложения (подарок,баллы, итд",
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True, null=True, upload_to="marketing_images"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Query_log",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "data_time",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата и время"
                    ),
                ),
                ("raw_text", models.TextField(verbose_name="Текс/данные запроса")),
            ],
        ),
        migrations.CreateModel(
            name="Question_answer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.TextField(verbose_name="Название вопроса")),
                ("description", models.TextField(verbose_name="Описание вопроса")),
                (
                    "link",
                    models.TextField(
                        blank=True, null=True, verbose_name="Ссылка на источник"
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True, null=True, upload_to="question_answer_images"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="User_tg",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "user_id",
                    models.CharField(
                        max_length=50, unique=True, verbose_name="id пользователя"
                    ),
                ),
                (
                    "user_name",
                    models.CharField(
                        max_length=128, unique=True, verbose_name="name пользователя"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="User_worker_ozon",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "user_id",
                    models.CharField(
                        max_length=50, unique=True, verbose_name="id ТГ работника"
                    ),
                ),
                (
                    "user_name",
                    models.CharField(
                        max_length=128, unique=True, verbose_name="name ТГ работника"
                    ),
                ),
                (
                    "access",
                    models.TextField(
                        blank=True, null=True, verbose_name="Активация пользователя"
                    ),
                ),
                (
                    "role",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="db.deportment_worker_ozon",
                        verbose_name="Роль",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Question_user",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("raw_text", models.TextField(verbose_name="Описание вопроса")),
                (
                    "manager_logic",
                    models.CharField(
                        max_length=50,
                        unique=True,
                        verbose_name="Результат ответа менеджера и закрытие вопроса",
                    ),
                ),
                (
                    "manager_text",
                    models.TextField(
                        blank=True, null=True, verbose_name="Описание ответа менеджера"
                    ),
                ),
                (
                    "manager_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="db.user_worker_ozon",
                        verbose_name="Назначенный менеджер",
                    ),
                ),
                (
                    "user_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="db.user_tg",
                        verbose_name="Пользователь",
                    ),
                ),
            ],
        ),
    ]
