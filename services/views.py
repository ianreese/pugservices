from django.shortcuts import render

from django.urls import path
from . import views

def junk_hauling(request):
    return render(request, "services/junk_hauling.html")

def pressure_washing(request):
    return render(request, "services/pressure_washing.html")
