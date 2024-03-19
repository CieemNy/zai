from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('filmlist/', views.ListFilm.as_view(), name="film-list"),
    path('filmlist/<int:pk>/', views.RetrieveFilm.as_view(), name="film-retrieve"),
    path('filmcreate/', views.CreateFilm.as_view(), name="film-create"),
]