import re

from django.db import models

NULLABLE = {"blank": True, "null": True}


def clean_title(title):
    return re.sub(r"[^\w]", "_", title)


def house_photo_upload_path(instance, filename):
    clean_house_title = clean_title(instance.house.title)
    return f"houses_photos/{clean_house_title}/{filename}"


class HeaderText(models.Model):
    title = models.CharField(max_length=100, verbose_name="Текст")
    is_active = models.BooleanField(
        default=False, verbose_name="Активный (начальный) текст"
    )

    class Meta:
        verbose_name = "Текст в header"
        verbose_name_plural = "Тексты в header"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.is_active:
            HeaderText.objects.filter(is_active=True).exclude(pk=self.pk).update(
                is_active=False
            )
        super().save(*args, **kwargs)


class House(models.Model):
    title = models.CharField(max_length=100, verbose_name="Короткое название")
    description = models.TextField(verbose_name="Описание дома")
    area = models.FloatField(verbose_name="Площадь дома (кв. м)")

    class Meta:
        verbose_name = "Дом"
        verbose_name_plural = "Дома"

    def __str__(self):
        return self.title


class HousePhoto(models.Model):
    house = models.ForeignKey(
        House, on_delete=models.CASCADE, related_name="photos", verbose_name="Дом"
    )
    photo = models.ImageField(
        upload_to=house_photo_upload_path, verbose_name="Фотография"
    )
    is_main = models.BooleanField(default=False, verbose_name="Главная фотография")

    def __str__(self):
        return f"Фото для дома {self.house.title}"

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["house", "is_main"],
                condition=models.Q(is_main=True),
                name="unique_main_photo_per_house",
            )
        ]
        verbose_name = "Фото домов"
        verbose_name_plural = "Фото домов"


class ContactInfo(models.Model):
    address = models.CharField(max_length=100, verbose_name="Адрес")
    phone = models.CharField(max_length=100, verbose_name="Номер телефона", **NULLABLE)
    email = models.CharField(max_length=100, verbose_name="Адрес почты", **NULLABLE)
    telegram = models.URLField(verbose_name="Ссылка на Telegram", **NULLABLE)
    whatsapp = models.URLField(verbose_name="Ссылка на WhatsApp", **NULLABLE)
    instagram = models.URLField(verbose_name="Ссылка на Instagram", **NULLABLE)

    def __str__(self):
        return f"{self.address}, {self.phone}"

    class Meta:
        verbose_name = "Контактная информация"
        verbose_name_plural = "Контактная информация"
