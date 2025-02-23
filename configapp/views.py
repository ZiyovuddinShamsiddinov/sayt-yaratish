from django.shortcuts import render

from configapp.models import *

def index0(request):
    cars=Car.objects.all()
    cars_model=Car_model.objects.all()

    context={
    "cars":cars,
    "cars_model":cars_model,
}
    return render(request,'News/index0.html',context=context)

def cars_model(request, model_id):
    cars = Car.objects.filter(model_id=model_id)
    cars_model=Car_model.objects.all()
    context = {
        "cars": cars,
        "cars_model": cars_model,
    }
    return render(request, 'News/car_model.html', context=context)


def car_about(request,model_id):
    car = Car.objects.get(pk=model_id)

    context = {
        "cars_about": car,
    }
    return render(request, 'car_new.html', context=context)