from django.contrib import admin
from django.utils.html import format_html

from houses.models import (Album, ContactInfo, HeaderText, House, Interior,
                           News, Photo)


class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 10
    fields = ("image", "description", "preview")
    readonly_fields = ("preview",)

    def preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="100" height="75" />', obj.image.url
            )
        return "Нет изображения"

    preview.short_description = "Превью"


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    search_fields = ("name",)
    inlines = [PhotoInline]


@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
        "created_at",
        "album_link",
        "main_photo_preview",
    )
    search_fields = ("name",)
    list_filter = ("created_at",)
    readonly_fields = ("main_photo_preview",)

    def album_link(self, obj):
        if obj.album:
            return format_html(
                '<a href="/admin/houses/album/{}/change/">{}</a>',
                obj.album.id,
                obj.album.name,
            )
        return "-"

    album_link.short_description = "Альбом"

    def main_photo_preview(self, obj):
        if obj.main_photo:
            return format_html(
                '<img src="{}" width="100" height="75" />', obj.main_photo.url
            )
        return "Нет фото"

    main_photo_preview.short_description = "Превью"


@admin.register(Interior)
class InteriorAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
        "created_at",
        "album_link",
        "main_photo_preview",
    )
    search_fields = ("name",)
    list_filter = ("created_at",)
    readonly_fields = ("main_photo_preview",)

    def album_link(self, obj):
        if obj.album:
            return format_html(
                '<a href="/admin/houses/album/{}/change/">{}</a>',
                obj.album.id,
                obj.album.name,
            )
        return "-"

    album_link.short_description = "Альбом"

    def main_photo_preview(self, obj):
        if obj.main_photo:
            return format_html(
                '<img src="{}" width="100" height="75" />', obj.main_photo.url
            )
        return "Нет фото"

    main_photo_preview.short_description = "Превью"


@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ("address", "phone", "email", "telegram", "whatsapp", "instagram")


@admin.register(HeaderText)
class HeaderTextAdmin(admin.ModelAdmin):
    list_display = ("title", "is_active")
    list_editable = ("is_active",)
    actions = ["set_active"]

    def set_active(self, request, queryset):
        HeaderText.objects.all().update(is_active=False)
        queryset.update(is_active=True)

    set_active.short_description = "Сделать активным выбранный текст"


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
        "created_at",
        "main_photo_preview",
    )
    search_fields = ("name",)
    list_filter = ("created_at",)
    readonly_fields = ("main_photo_preview",)

    def main_photo_preview(self, obj):
        if obj.main_photo:
            return format_html(
                '<img src="{}" width="100" height="75" />', obj.main_photo.url
            )
        return "Нет фото"

    main_photo_preview.short_description = "Превью"
