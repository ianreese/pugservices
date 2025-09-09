from django.urls import path
from . import views

urlpatterns = [
    path("junk-hauling/", views.junk_hauling, name="junk_hauling"),
    path("pressure-washing/", views.pressure_washing, name="pressure_washing"),
]

