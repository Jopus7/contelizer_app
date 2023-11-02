from django.urls import path
from . import views

app_name = 'pesel'

urlpatterns = [
    path('', views.pesel, name='pesel'),
]