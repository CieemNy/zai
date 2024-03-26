from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .serializers import *
from .permissions import IsOwnerOrReadOnly


class ListCreateFilm(generics.ListAPIView):
    # queryset = Film.objects.all().order_by('-rok','tytul')
    serializer_class = FilmSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'tytul', 'rok', 'opis']
    # search_fields = ['tytul', 'opis', 'rok']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    # def get_queryset(self):
    #     queryset = Film.objects.all().order_by('-rok', 'tytul')
    #     tytul = self.request.query_params.get('tytul')
    #     id = self.request.query_params.get('id')
    #     if tytul is not None:
    #         queryset = queryset.filter(tytul__startswith=tytul)
    #     if id is not None:
    #         queryset = queryset.filter(id__exact=id)
    #     return queryset


class RetrieveUpdateDestroyFilm(generics.RetrieveUpdateDestroyAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
    name = "retrieve-film"
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class UserCreateList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializerShort


class UserRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializerShort


class ExtraInfoCreateList(generics.ListCreateAPIView):
    queryset = ExtraInfo.objects.all()
    serializer_class = ExtraInfoSerializer


class ExtraInfoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = ExtraInfo.objects.all()
    serializer_class = ExtraInfoSerializer


class OcenaCreateList(generics.ListCreateAPIView):
    queryset = Ocena.objects.all()
    serializer_class = OcenaSerializer


class OcenaRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ocena.objects.all()
    serializer_class = OcenaSerializer


class AktorCreateList(generics.ListCreateAPIView):
    queryset = Aktor.objects.all()
    serializer_class = AktorSerializer


class AktorRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Aktor.objects.all()
    serializer_class = AktorSerializer
