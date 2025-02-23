from tkinter.constants import CASCADE
from django.utils.timezone import now
from django.db import models
from django.utils import timezone
from django.template.context_processors import request

class Car_model(models.Model):
    title=models.CharField(max_length=50)
    birth_date=models.DateField(blank=True)
    created_ed=models.DateTimeField(auto_now_add=True)
    update_ed=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name="Car_model"
        verbose_name_plural="Car_models"
        ordering = ['created_ed']

class Car(models.Model):
    title=models.CharField(max_length=50,null=True)
    color=models.CharField(max_length=15,null=True,blank=True)
    model=models.ForeignKey(Car_model,on_delete=models.CASCADE)
    ot_kuchi=models.CharField(max_length=10)
    narxi=models.CharField(max_length=50)
    yili=models.CharField(max_length=15)
    def __str__(self):
        return self.title

