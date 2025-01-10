from django.db import models


class HouseSection(models.Model):
    description = models.TextField(max_length=250, help_text="Общее описание раздела")

    def __str__(self):
        return f"Раздел 'Дома' (описание: {self.description[:50]}...)"


class House(models.Model):
    section = models.ForeignKey(
        HouseSection,
        on_delete=models.CASCADE,
        related_name="houses",
        verbose_name="Раздел",
    )
    title = models.CharField(max_length=100, verbose_name="Короткое название")
    description = models.TextField(verbose_name="Описание дома")
    area = models.FloatField(verbose_name="Площадь дома (кв. м)")
    style = models.CharField(max_length=100, verbose_name="Стиль дома")

    def __str__(self):
        return self.title


class HousePhoto(models.Model):
    house = models.ForeignKey(
        House, on_delete=models.CASCADE, related_name="photos", verbose_name="Дом"
    )
    photo = models.ImageField(
        upload_to=f"house_photos/{house}", verbose_name="Фотография"
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
