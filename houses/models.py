from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

from houses.utils.file_path import album_photo_path, main_photo_path

NULLABLE = {"blank": True, "null": True}


class Album(models.Model):
    """Модель альбома"""

    name = models.CharField(max_length=100, verbose_name="Название альбома")
    description = models.CharField(max_length=255, verbose_name="Описание")

    class Meta:
        verbose_name = "Альбом"
        verbose_name_plural = "Альбомы"

    def __str__(self):
        return self.name


class Photo(models.Model):
    """Модель фотографии"""

    album = models.ForeignKey(
        Album, on_delete=models.CASCADE, related_name="photos", verbose_name="Альбом"
    )
    image = ProcessedImageField(
        upload_to=album_photo_path,
        processors=[ResizeToFill(800, 600)],
        format="JPEG",
        options={"quality": 80},
        verbose_name="Фото",
    )
    description = models.CharField(max_length=255, verbose_name="Описание", **NULLABLE)

    class Meta:
        verbose_name = "Фотография"
        verbose_name_plural = "Фотографии"

    def __str__(self):
        return f"Фото {self.id} из альбома {self.album.name}"


class House(models.Model):
    """Модель дома"""

    name = models.CharField(max_length=100, verbose_name="Название дома")
    description = models.TextField(verbose_name="Описание")
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата и время создания", **NULLABLE
    )
    main_photo = ProcessedImageField(
        upload_to=main_photo_path,
        processors=[ResizeToFill(800, 600)],
        format="JPEG",
        options={"quality": 80},
        verbose_name="Фото",
        **NULLABLE,
    )
    album = models.OneToOneField(
        "Album", on_delete=models.SET_NULL, **NULLABLE, verbose_name="Альбом"
    )

    class Meta:
        ordering = ("-created_at",)
        verbose_name = "Дом"
        verbose_name_plural = "Дома"

    def __str__(self):
        return self.name


class Interior(models.Model):
    """Модель интерьера"""

    name = models.CharField(max_length=50, verbose_name="Название интерьера")
    description = models.CharField(max_length=255, verbose_name="Описание")
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата и время создания"
    )
    main_photo = ProcessedImageField(
        upload_to=main_photo_path,
        processors=[ResizeToFill(800, 600)],
        format="JPEG",
        options={"quality": 80},
        verbose_name="Фото",
        **NULLABLE,
    )
    album = models.OneToOneField(
        "Album", on_delete=models.SET_NULL, **NULLABLE, verbose_name="Альбом"
    )

    class Meta:
        ordering = ("-created_at",)
        verbose_name = "Интерьер"
        verbose_name_plural = "Интерьеры"

    def __str__(self):
        return self.name


class News(models.Model):
    """Модель новости"""

    name = models.CharField(max_length=100, verbose_name="Название новости")
    description = models.TextField(verbose_name="Описание")
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата и время создания"
    )
    main_photo = ProcessedImageField(
        upload_to=main_photo_path,
        processors=[ResizeToFill(800, 600)],
        format="JPEG",
        options={"quality": 80},
        verbose_name="Фото",
        **NULLABLE,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"


class ContactInfo(models.Model):
    """Модель контактной информации"""

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


class HeaderText(models.Model):
    """Модель для текста в header на главной странице"""

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
