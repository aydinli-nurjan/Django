from django.urls import path

from .views import *

urlpatterns = [
    # path('html/', html),
    # path('home/<int:catid>/', index),
    # path('about/<slug:cat>/', about),
    path('home/', home),
    path('contact/', contact),
    path('single-page/', single_page),
]
