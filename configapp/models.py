from django.db import models

class Categories(models.Model):
    title=models.CharField(max_length=50)

    def __str__(self):
        return self.title

class News(models.Model):
    category_id=models.ForeignKey(Categories,on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    context = models.TextField(blank=True)
    created_ed = models.DateTimeField(auto_now_add=True)
    updated_ed = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    is_bool = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Aftosalon(models.Model):
    # Aftosalon_id = models.AutoField(primary_key=True)
    title=models.CharField(max_length=50)
    context=models.TextField(blank=True)
    created=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name="Aftosolon"
        verbose_name_plural="Aftosolons"
        ordering = ['-created']

    def __str__(self):
        return self.title

class Car(models.Model):
    model=models.CharField(max_length=50)
    ot_kuchi=models.CharField(max_length=10)
    narxi=models.CharField(max_length=50)
    yili=models.CharField(max_length=4)

