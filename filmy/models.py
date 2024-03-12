from django.db import models


class Film(models.Model):
    tytul = models.CharField(max_length=50)
    opis = models.TextField(default="")
    producent = models.CharField(max_length=255)
    rezyser = models.CharField(max_length=255)
    rok = models.IntegerField(blank=False)
    ocena = models.IntegerField(default=0)

    def __str__(self):
        return "{} ({})".format(self.tytul, str(self.rok))
