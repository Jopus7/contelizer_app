from django.urls import path
from . import views

app_name = 'files'

urlpatterns = [
    path('', views.file_upload, name='upload'),
    path('display/<str:name>/', views.display, name='display'),
]
