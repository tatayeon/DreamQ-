from django.urls import path, include 
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("select", views.map),  
    path("time", views.time),
    path("graph", views.graph),
    path("overlay", views.overlay),
    path("", views.select),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
