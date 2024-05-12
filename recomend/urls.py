from . import views
from django.urls import path, include

urlpatterns = [
    path("", views.index), 
    path("family/", views.family),
    path("couple/", views.couple),
    path("friend/", views.friend),
    # path("couple/<str:detail>", views.detail),
    path("family/detail/<str:type>/", views.detail),
    path("couple/detail/<str:type>/", views.detail),
    path("friend/detail/<str:type>/", views.detail),


]   