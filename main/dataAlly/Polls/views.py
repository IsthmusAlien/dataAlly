from django.shortcuts import render

def Polls(request):
    return render(request, 'polls.html')
