# Generated by Django 5.1.4 on 2025-01-28 18:33

import django.db.models.deletion
import houses.utils.file_path
import imagekit.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Album",
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
                    "name",
                    models.CharField(max_length=100, verbose_name="Название альбома"),
                ),
                (
                    "description",
                    models.CharField(max_length=255, verbose_name="Описание"),
                ),
            ],
            options={
                "verbose_name": "Альбом",
                "verbose_name_plural": "Альбомы",
            },
        ),
        migrations.CreateModel(
            name="ContactInfo",
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
                ("address", models.CharField(max_length=100, verbose_name="Адрес")),
                (
                    "phone",
                    models.CharField(
                        blank=True,
                        max_length=100,
                        null=True,
                        verbose_name="Номер телефона",
                    ),
                ),
                (
                    "email",
                    models.CharField(
                        blank=True,
                        max_length=100,
                        null=True,
                        verbose_name="Адрес почты",
                    ),
                ),
                (
                    "telegram",
                    models.URLField(
                        blank=True, null=True, verbose_name="Ссылка на Telegram"
                    ),
                ),
                (
                    "whatsapp",
                    models.URLField(
                        blank=True, null=True, verbose_name="Ссылка на WhatsApp"
                    ),
                ),
                (
                    "instagram",
                    models.URLField(
                        blank=True, null=True, verbose_name="Ссылка на Instagram"
                    ),
                ),
            ],
            options={
                "verbose_name": "Контактная информация",
                "verbose_name_plural": "Контактная информация",
            },
        ),
        migrations.CreateModel(
            name="HeaderText",
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
                ("title", models.CharField(max_length=100, verbose_name="Текст")),
                (
                    "is_active",
                    models.BooleanField(
                        default=False, verbose_name="Активный (начальный) текст"
                    ),
                ),
            ],
            options={
                "verbose_name": "Текст в header",
                "verbose_name_plural": "Тексты в header",
            },
        ),
        migrations.CreateModel(
            name="House",
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
                    "name",
                    models.CharField(max_length=100, verbose_name="Название дома"),
                ),
                (
                    "description",
                    models.CharField(max_length=255, verbose_name="Описание"),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True,
                        null=True,
                        verbose_name="Дата и время создания",
                    ),
                ),
                (
                    "main_photo",
                    imagekit.models.fields.ProcessedImageField(
                        blank=True,
                        null=True,
                        upload_to=houses.utils.file_path.main_photo_path,
                        verbose_name="Фото",
                    ),
                ),
                (
                    "album",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="houses.album",
                        verbose_name="Альбом",
                    ),
                ),
            ],
            options={
                "verbose_name": "Дом",
                "verbose_name_plural": "Дома",
                "ordering": ("-created_at",),
            },
        ),
        migrations.CreateModel(
            name="Interior",
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
                    "name",
                    models.CharField(max_length=50, verbose_name="Название интерьера"),
                ),
                (
                    "description",
                    models.CharField(max_length=255, verbose_name="Описание"),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата и время создания"
                    ),
                ),
                (
                    "main_photo",
                    imagekit.models.fields.ProcessedImageField(
                        blank=True,
                        null=True,
                        upload_to=houses.utils.file_path.main_photo_path,
                        verbose_name="Фото",
                    ),
                ),
                (
                    "album",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="houses.album",
                        verbose_name="Альбом",
                    ),
                ),
            ],
            options={
                "verbose_name": "Интерьер",
                "verbose_name_plural": "Интерьеры",
                "ordering": ("-created_at",),
            },
        ),
        migrations.CreateModel(
            name="Photo",
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
                    "image",
                    imagekit.models.fields.ProcessedImageField(
                        upload_to=houses.utils.file_path.album_photo_path,
                        verbose_name="Фото",
                    ),
                ),
                (
                    "description",
                    models.CharField(
                        blank=True, max_length=255, null=True, verbose_name="Описание"
                    ),
                ),
                (
                    "album",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="photos",
                        to="houses.album",
                        verbose_name="Альбом",
                    ),
                ),
            ],
            options={
                "verbose_name": "Фотография",
                "verbose_name_plural": "Фотографии",
            },
        ),
    ]
