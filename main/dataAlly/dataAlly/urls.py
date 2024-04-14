from django.contrib import admin
from django.urls import path
from Home.views import Home
from Database.views import Database
from Models.views import Models
from Login.views import Login
from Signup.views import Signup
from Polls.views import Polls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home),
    path('database/', Database),
    path('models/', Models),
    path('login/', Login),
    path('signup/', Signup),
    path('polls/', Polls),
]
