from django.contrib import admin
from .models import Film, ExtraInfo, Ocena, Aktor


class FilmAdmin(admin.ModelAdmin):
    list_display = ['id', 'tytul', 'opis', 'producent', 'rezyser', 'rok']


class ExtraInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'czas_trwania', 'gatunek', 'filmy']


class OcenaAdmin(admin.ModelAdmin):
    list_display = ['id', 'recenzja', 'gwiazdki', 'film']


class AktorAdmin(admin.ModelAdmin):
    list_display = ['id', 'imie', 'nazwisko', 'filmy', 'owner']

    def filmy(self, obj):
        filmy = obj.Film.all()
        return ", ".join([film.tytul for film in filmy])


admin.site.register(Film, FilmAdmin)
admin.site.register(ExtraInfo, ExtraInfoAdmin)
admin.site.register(Ocena, OcenaAdmin)
admin.site.register(Aktor, AktorAdmin)

