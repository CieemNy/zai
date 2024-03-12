from datetime import datetime

from django.db import models


class Film(models.Model):
    tytul = models.CharField(max_length=50)
    opis = models.CharField(max_length=255)
    producent = models.CharField(max_length=255)
    rezyser = models.CharField(max_length=255)
    premiera = models.DateTimeField(default=datetime.now, blank=True)
    ocena = models.IntegerField(default=0)