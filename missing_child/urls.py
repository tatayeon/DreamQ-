from django.urls import path, include 
from . import views

urlpatterns = [
    path("", views.mia),  
    path("<int:pk>", views.mia_info),
]