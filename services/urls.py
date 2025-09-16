from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="index"),
    path("lawn/", views.lawn, name="lawn"),
    path("cleaning/", views.cleaning, name="cleaning"),
    path("carpet/", views.carpet, name="carpet"),
    path("junk/", views.junk, name="junk"),
    path("pressure/", views.pressure, name="pressure"),
]

