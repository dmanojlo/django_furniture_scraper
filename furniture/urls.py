from django.urls import path, include, re_path
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views
from .views import mima, emezzeta

app_name = 'furniture' # za url putanju do appa

urlpatterns = [
     path('mima/', mima, name='mima'),
     path('emezzeta/', emezzeta, name='emezzeta'),

]
