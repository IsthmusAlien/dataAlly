from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from Home.views import Home
from Database.views import Dataset
from Models.views import Models
from Login.views import Login
from Signup.views import Signup
from Polls.views import Polls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home),
    path('database/', Dataset),
    path('models/', Models),
    path('login/', Login),
    path('signup/', Signup),
    path('polls/', Polls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
