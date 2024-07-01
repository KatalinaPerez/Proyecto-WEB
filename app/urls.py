from django.urls import path
from .views import home, mangas, comics

urlpatterns = [
    path('',home, name="home"),
    path('mangas/', mangas, name="mangas"),
    path('comics/',comics, name="comics")
]