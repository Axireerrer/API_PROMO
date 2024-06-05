from django.contrib import admin
from api.models import Advert


# Модель в админке
@admin.register(Advert)
class AdvertAdmin(admin.ModelAdmin):
    list_display = ['title', 'advert_id', 'author', 'views_count', 'position']

