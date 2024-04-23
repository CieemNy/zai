from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, DjangoModelPermissions
from .serializers import *
from .permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.db.models import Count, Q, Max, Min


class ListCreateFilm(generics.ListAPIView):
    queryset = Film.objects.all()
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
    # permission_classes = [DjangoModelPermissions]
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializerShort

    def create(self, request, *args, **kwargs):
        user = self.request.user
        if user.is_superuser:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        else:
            return Response(data=None, status=status.HTTP_403_FORBIDDEN)


class UserRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [DjangoModelPermissions]
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializerShort

    def update(self, request, *args, **kwargs):
        user = self.request.user
        if user.is_superuser:
            partial = kwargs.pop('partial', False)
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)

            if getattr(instance, '_prefetched_objects_cache', None):
                instance._prefetched_objects_cache = {}

            return Response(serializer.data)
        else:
            return Response(data=None, status=status.HTTP_403_FORBIDDEN)

    def destroy(self, request, *args, **kwargs):
        user = self.request.user
        if user.is_superuser:
            instance = self.get_object()
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)


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


class statRezyserLiczbaFilmow(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = statRezyser
    rezyserOK = set([r.rezyser for r in Film.objects.filter(rezyser__isnull=False)])
    rf = []

    for r in rezyserOK:
        rf.append([r,Film.objects.filter(rezyser=r).count()])

    rf.sort(key=lambda a: a[1], reverse=True)
    queryset = rf


class statFilmyLiczbaOcen(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = statOceny
    filmy = Film.objects.filter(ocena__id__isnull=False).annotate(l_ocen=Count("ocena__id")).order_by("-l_ocen")
    fo = []

    for f in filmy:
        fo.append([f.tytul, f.l_ocen])

    fo.sort(key=lambda a: a[1], reverse=True)
    queryset = fo


class statFilmyKategorieDobrySlaby(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = statOceny
    dobry = Count("ocena__id", filter=Q(ocena__gwiazdki__gt=5))
    slaby = Count("ocena__id", filter=Q(ocena__gwiazdki__lte=5))
    filmy = Film.objects.filter(ocena__id__isnull=False).annotate(dobry=dobry).annotate(slaby=slaby)
    fk = []

    for f in filmy:
        fk.append([f.tytul, f.dobry, f.slaby])

    queryset = fk


class statFilmyGwiazdkiMaxMin(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = statOceny
    gmax = Max("ocena__gwiazdki")
    gmin = Min("ocena__gwiazdki")
    filmy = Film.objects.filter(ocena__id__isnull=False).annotate(gmax=gmax).annotate(gmin=gmin)
    fk = []

    for f in filmy:
        fk.append([f.tytul, f.gmax, f.gmin])

    fk.sort(key=lambda a: a[1], reverse=True)
    queryset = fk


class statFilmyBezOcen(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = FilmSerializer
    queryset = Film.objects.filter(ocena__id__isnull=True)


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'Użytkownicy': reverse('UserList', request=request, format=format),
        'Wszystkie filmy': reverse('film-list', request=request, format=format),
        'Informacje dodatkowe': reverse('ExtraInfoCreateList', request=request, format=format),
        'Wszystkie oceny': reverse('OcenaCreateList', request=request, format=format),
        'Wszyscy aktorzy': reverse('AktorCreateList', request=request, format=format),
        'Statystyki_rezyser_liczba_filmow': reverse('statRezyserLiczbaFilmow', request=request, format=format),
        'Statystyki_filmy_liczba_ocen': reverse('statFilmyLiczbaOcen', request=request, format=format),
        'Statystyki_filmy_bez_ocen': reverse('statFilmyBezOcen', request=request, format=format),
        'Statystyki_filmy_dobre_slabe': reverse('statFilmyKategorieDobrySlaby', request=request, format=format),
        'Statystyki_filmy_gwiazdki_max_min': reverse('statFilmyGwiazdkiMaxMin', request=request, format=format),
    })