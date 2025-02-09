import os
import uuid

from django.utils.deconstruct import deconstructible


@deconstructible
class UploadToPath:
    def __init__(self, sub_path):
        self.sub_path = sub_path

    def __call__(self, instance, filename):
        ext = filename.split(".")[-1]
        filename = f"{uuid.uuid4().hex}.{ext}"
        return os.path.join(self.sub_path, filename)


def album_photo_path(instance, filename):
    """Путь для фотографий в альбомах"""
    return UploadToPath(f"houses/albums/album_{instance.album.id}")(instance, filename)


def main_photo_path(instance, filename):
    """Путь для главных фотографий моделей"""
    model_name = instance._meta.model_name
    return UploadToPath(f"houses/main_photo/{model_name}_main_photo")(
        instance, filename
    )
