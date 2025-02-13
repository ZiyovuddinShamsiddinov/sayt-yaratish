from django.http import HttpResponse
from django.shortcuts import render
from configapp.models import *

def index(request):
    aftosalon=Aftosalon.objects.all()

    context={
        "aftosalon":aftosalon,
        "title":"Aftosalon"
    }
    db={
        "title":"Aftasalon",
        "manzil":"Uzbekistan",
        "telefon":"+998965236514",
    }
    return render(request, 'News/index.html', context=context)
#     news=News.objects.all()
#
#     context={
#         "news":news,
#         "title":"News Title"
#     }
#     db={
#         "name":"Usmon Xolmurodov",
#         "phone":"+998933941209",
#         "age":16,
#         "pisyun":"sredniy",
#         "lichnaya infa":"bolshoy bolshoy sikret"
#     }
#     return render(request,'News/index.html',context=context)

def index2(request):
    car = Car.objects.all()

    context = {
        "car": car,
        "title": "Car"
    }
    db = {
        "name": "BMW",
        "ot_kuchi": 1500,
        "model": "X11",
    }
    return render(request, 'News/index.html', context=context)
