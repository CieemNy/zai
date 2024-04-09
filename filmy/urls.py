from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', api_root),
    path('filmlist/', views.ListCreateFilm.as_view(), name="film-list"),
    path('filmlist/<int:pk>/', views.RetrieveUpdateDestroyFilm.as_view(), name="film-retrieve"),
    path('filmcreate/', views.ListCreateFilm.as_view(), name="film-create"),
    path('filmdelete/<int:pk>/', views.RetrieveUpdateDestroyFilm.as_view(), name="film-destroy"),
    path('filmupdate/<int:pk>/', views.RetrieveUpdateDestroyFilm.as_view(), name="film-update"),
    path('extrainfo/', ExtraInfoCreateList.as_view(), name='ExtraInfoCreateList'),
    path('extrainfo/<int:pk>/', ExtraInfoRetrieveUpdateDestroy.as_view(), name='ExtraInfoRetrieveUpdateDestroy'),
    path('ocena/', OcenaCreateList.as_view(), name='OcenaCreateList'),
    path('ocena/<int:pk>/', OcenaRetrieveUpdateDestroy.as_view(), name='OcenaRetrieveUpdateDestroy'),
    path('aktor/', AktorCreateList.as_view(), name='AktorCreateList'),
    path('aktor/<int:pk>/', AktorRetrieveUpdateDestroy.as_view(), name='AktorRetrieveUpdateDestroy'),
    path('userlist/', UserCreateList.as_view(), name='UserList'),
    path('usercreatelist/', UserCreateList.as_view(), name='UserCreateList'),
    path('user/<int:pk>/', UserRetrieveUpdateDestroy.as_view(), name='UserRetrieveUpdateDestroy')
]
