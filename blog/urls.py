from . import views
from django.urls import path, include

urlpatterns = [
    path("", views.index), 
    path("<int:pk>/", views.singpage) #/blog/숫자가 들어오면
]   