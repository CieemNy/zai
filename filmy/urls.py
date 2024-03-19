from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('filmlist/', views.ListFilm.as_view(), name="film-list"),
    path('filmlist/<int:pk>/', views.RetrieveFilm.as_view(), name="film-retrieve"),
    path('filmcreate/', views.CreateFilm.as_view(), name="film-create"),
    path('filmdelete/<int:pk>/', views.DestroyFilm.as_view(), name="film-destroy"),
    path('filmupdate/<int:pk>/', views.UpdateFilm.as_view(), name="film-update"),
    path('userlist/', UserList.as_view(), name='UserList'),
    path('usercreatelist/', UserCreateList.as_view(), name='UserCreateList')
]