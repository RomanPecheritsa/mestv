from django.contrib import admin

from houses.models import House, HousePhoto, HouseSection


class HousePhotoInline(admin.TabularInline):
    model = HousePhoto
    extra = 1


@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    list_display = ("title", "section", "area", "style")
    inlines = [HousePhotoInline]


@admin.register(HouseSection)
class HouseSectionAdmin(admin.ModelAdmin):
    list_display = ("description",)


@admin.register(HousePhoto)
class HousePhotoAdmin(admin.ModelAdmin):
    list_display = ("house", "photo", "is_main")
