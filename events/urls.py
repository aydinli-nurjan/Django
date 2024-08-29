from django.urls import path 

from .views import *

urlpatterns = [
    path('home/', index),
    path('about/', about),
    path('contact/', contact),
    path('team/', team),
]