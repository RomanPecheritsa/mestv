from django.contrib import admin

from houses.models import ContactInfo, HeaderText, House, HousePhoto


@admin.register(HeaderText)
class HeaderTextAdmin(admin.ModelAdmin):
    list_display = ("title", "is_active")
    fields = ("title", "is_active")


class HousePhotoInline(admin.TabularInline):
    model = HousePhoto
    extra = 1


@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    list_display = ("title", "area")
    inlines = [HousePhotoInline]


@admin.register(HousePhoto)
class HousePhotoAdmin(admin.ModelAdmin):
    list_display = ("house", "photo", "is_main")


@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ("address", "phone", "email", "telegram", "whatsapp", "instagram")
