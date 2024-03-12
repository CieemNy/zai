from django.contrib import admin
from .models import Film


class FilmAdmin(admin.ModelAdmin):
    list_display = ['id', 'tytul', 'opis', 'producent', 'rezyser', 'rok', 'ocena']


admin.site.register(Film, FilmAdmin)

