from rest_framework import generics
from .serializers import *


class ListFilm(generics.ListAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
    name = "list-film"


class RetrieveFilm(generics.RetrieveAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
    name = "retrieve-film"


class CreateFilm(generics.ListCreateAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
    name = "create-film"


class DestroyFilm(generics.DestroyAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
    name = "destroy-film"


class UpdateFilm(generics.UpdateAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
    name = "update-film"


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializerShort


class UserCreateList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

