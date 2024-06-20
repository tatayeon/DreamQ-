from django.urls import path, include 
from . import views

urlpatterns = [
    path("", views.parking),  
    path("<int:pk>", views.congestion),
]