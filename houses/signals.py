import os
import shutil

from django.conf import settings
from django.db.models.signals import post_delete
from django.dispatch import receiver

from .models import Album, House, Interior, News, Photo


@receiver(post_delete, sender=Album)
def delete_album_photos(sender, instance, **kwargs):
    """Удаляет папку с альбомом и все фото в ней при удалении альбома"""
    album_folder = os.path.join(
        settings.MEDIA_ROOT, f"houses/albums/album_{instance.id}"
    )
    if os.path.exists(album_folder):
        shutil.rmtree(album_folder, ignore_errors=True)


@receiver(post_delete, sender=Photo)
def delete_photo_file(sender, instance, **kwargs):
    """Удаляет файл фотографии при удалении записи"""
    if instance.image:
        image_path = instance.image.path
        if os.path.exists(image_path):
            os.remove(image_path)


def delete_main_photo(instance):
    """Удаляет главное фото при удалении объекта"""
    if instance.main_photo:
        image_path = instance.main_photo.path
        if os.path.exists(image_path):
            os.remove(image_path)


@receiver(post_delete, sender=House)
@receiver(post_delete, sender=Interior)
@receiver(post_delete, sender=News)
def delete_main_photo_on_delete(sender, instance, **kwargs):
    """Удаляет главное фото при удалении House, Interior, News"""
    delete_main_photo(instance)
