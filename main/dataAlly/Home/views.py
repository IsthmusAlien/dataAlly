from django.shortcuts import render
from Database.models import Database
from Models.models import Models

def Home(request):
    databases = Database.objects.all().order_by('-db_rating')[:10]
    models = Models.objects.all().order_by('-md_rating')[:10]
    return render(request, 'home.html', {'databases': databases, 'models': models})
