# Generated by Django 5.1.4 on 2025-01-13 11:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="HouseSection",
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
                    "title",
                    models.CharField(max_length=50, verbose_name="Название раздела"),
                ),
                (
                    "description",
                    models.TextField(
                        max_length=250, verbose_name="Общее описание раздела"
                    ),
                ),
            ],
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
                    "title",
                    models.CharField(max_length=100, verbose_name="Короткое название"),
                ),
                ("description", models.TextField(verbose_name="Описание дома")),
                ("area", models.FloatField(verbose_name="Площадь дома (кв. м)")),
                ("style", models.CharField(max_length=100, verbose_name="Стиль дома")),
                (
                    "section",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="houses",
                        to="houses.housesection",
                        verbose_name="Раздел",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="HousePhoto",
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
                    "photo",
                    models.ImageField(
                        upload_to="house_photos/<django.db.models.fields.related.ForeignKey>",
                        verbose_name="Фотография",
                    ),
                ),
                (
                    "is_main",
                    models.BooleanField(
                        default=False, verbose_name="Главная фотография"
                    ),
                ),
                (
                    "house",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="photos",
                        to="houses.house",
                        verbose_name="Дом",
                    ),
                ),
            ],
            options={
                "constraints": [
                    models.UniqueConstraint(
                        condition=models.Q(("is_main", True)),
                        fields=("house", "is_main"),
                        name="unique_main_photo_per_house",
                    )
                ],
            },
        ),
    ]
