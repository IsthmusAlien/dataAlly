from django.shortcuts import render
from Database.models import Database

def Home(request):
    databases = Database.objects.all().order_by('-db_rating')[:10]
    return render(request, 'home.html', {'databases': databases})
