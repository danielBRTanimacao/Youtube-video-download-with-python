from django.urls import path
from app_downloader import views

urlpatterns = [
    path('', views.home, name='home')
    # path('forms/')
]
