from django.contrib.auth.models import User
from django.db import models


class Film(models.Model):
    tytul = models.CharField(max_length=50)
    opis = models.TextField(default="")
    producent = models.CharField(max_length=255)
    rezyser = models.CharField(max_length=255)
    rok = models.IntegerField(blank=False)

    def __str__(self):
        return "{} ({})".format(self.tytul, str(self.rok))


class ExtraInfo(models.Model):
    GATUNEK = {
        (0, 'Inne'),
        (1, 'Horror'),
        (2, 'Komedia'),
        (3, 'Sci-fi'),
        (4, 'Dramat')
    }
    czas_trwania = models.PositiveSmallIntegerField(null=True, blank=True)
    gatunek = models.PositiveSmallIntegerField(choices=GATUNEK, null=True, blank=True)
    filmy = models.OneToOneField(Film, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.reprezentacja()

    def reprezentacja(self):
        for g in list(self.GATUNEK):
            if g[0] == self.gatunek:
                gok = g[1]
        return "Id zestawu: {}, film: {}, gatunek: {}, czas trwania: {}, reżyser: {}".format(
            self.id, self.filmy.tytul, gok, self.czas_trwania, self.filmy.rezyser)


class Ocena(models.Model):
    recenzja = models.TextField(default="", blank=True)
    gwiazdki = models.PositiveSmallIntegerField(default=5)
    film = models.ForeignKey(Film, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        rec = self.recenzja[:20] + ' ...'
        return "Film: {}, gwiazdki: {}, recenzja: {}".format(self.film.tytul, str(self.gwiazdki), rec)


class Aktor(models.Model):
    imie = models.CharField(max_length=32)
    nazwisko = models.CharField(max_length=32)
    filmy = models.ManyToManyField(Film, blank=True)
    owner = models.ForeignKey(User, related_name='aktorzy', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return "{} {}, gra w {} filmach z bazy danych".format(self.imie, self.nazwisko, str(self.filmy.count()))