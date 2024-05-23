from django.shortcuts import render
from .models import Database

def Dataset(request):
    datasets = Database.objects.all().order_by('db_type')
    data = {"datasets": datasets}
    return render(request, 'database.html', data)
