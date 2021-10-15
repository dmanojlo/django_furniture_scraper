from django.urls import path, include, re_path
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views
from .views import home

app_name = 'furniture' # za url putanju do appa

urlpatterns = [
     path('home/', home, name='home'),

]
