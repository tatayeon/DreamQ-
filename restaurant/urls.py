from django.urls import path, include 
from . import views

urlpatterns = [
    path("", views.rest),
      path("<int:pk>", views.rest_detail),
]