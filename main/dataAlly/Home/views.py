from django.shortcuts import render
from Database.models import Database

def Home(request):
    databases = Database.objects.all()
    return render(request, 'home.html', {'databases': databases})
