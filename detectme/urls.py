from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('video_feed/', views.video_feed, name='video_feed'),
    path('get_people_count', views.get_people_count, name='get_people_count'),
]