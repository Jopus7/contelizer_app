from django.urls import path
from . import views

app_name = 'files'

urlpatterns = [
    path('', views.file_upload, name='file_upload'),
]
