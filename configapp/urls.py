from django.contrib import admin
from django.urls import path,include
from configapp.views import *

urlpatterns = [
    path('aftosalon/' , index, name='aftosalon'),
    path('car/', index2 ),
]
