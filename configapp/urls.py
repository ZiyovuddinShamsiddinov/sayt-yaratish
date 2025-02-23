from tkinter.font import names

from django.contrib import admin
from django.urls import path
from configapp.views import *

urlpatterns = [
    path("all/" ,index0,name="home"),
    path("car_about/<int:model_id>", car_about,name="car_about"),
    path("cars_model/<int:model_id>", cars_model, name="cars_model"),

]
