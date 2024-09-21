from django.urls import path
from news.models import News
from .views import *

urlpatterns = [
    # path('html/', html),
    # path('home/<int:catid>/', index),
    # path('about/<slug:cat>/', about),
    path('home/', home, name='home'),
    path('contact/', contact,name='contact'),
    path('single-page/', single_page,name='single-page'),
]
