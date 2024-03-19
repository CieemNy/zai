from rest_framework import generics
from models import *
from serializers import *


class ListFilm(generics.ListAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
    name = "list-film"


class RetrieveFilm(generics.RetrieveAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
    name = "retrieve-film"


class CreateFilm(generics.ListCreateAPIView):
    serializer_class = FilmSerializer
    name = "create-film"

