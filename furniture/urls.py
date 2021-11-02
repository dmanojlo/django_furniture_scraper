from django.urls import path, include, re_path
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views
from .views import mima, emezzeta, lesnina, prima, harvey, home

app_name = 'furniture' # za url putanju do appa

urlpatterns = [
     path('home/', home, name='home'),
     path('mima/', mima, name='mima'),
     path('emezzeta/', emezzeta, name='emezzeta'),
     path('lesnina/', lesnina, name='lesnina'),
     path('prima/', prima, name='prima'),
     path('harvey/', harvey, name='harvey'),
]
