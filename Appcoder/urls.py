from django.urls import path 
from .views import * 

urlpatterns = [
    path("",inicio),
    path("madre/", madre),
    path("sobrino/", sobrino),
    path("sobrina/", sobrina),
]