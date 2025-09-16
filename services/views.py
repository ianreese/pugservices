from django.shortcuts import render

def home(request):
    return render(request, "index.html")

def lawn(request):
    return render(request, "lawn_care.html")

def cleaning(request):
    return render(request, "house_cleaning.html")

def carpet(request):
    return render(request, "carpet_cleaning.html")

def junk(request):
    return render(request, "junk_removal.html")

def pressure(request):
    return render(request, "pressure_washing.html")

