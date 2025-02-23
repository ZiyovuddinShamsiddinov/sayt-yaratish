from django.contrib import admin
from .models import *

# class CategoriesAdmin(admin.ModelAdmin):
#     list_display = ('title','id')
#     list_display_links = ['title']
#     search_fields = ['title']
    # list_editable = ['is_bool']

# class AftosalonAdmin(admin.ModelAdmin):
#     list_display = ('title','id')
#     list_display_links = ['title']
#     search_fields = ['title']
#     # list_editable = ['is_bool']

class CarAdmin(admin.ModelAdmin):
    list_display = ('title','id')
    list_display_links = ['title']
    search_fields = ['title']
    # list_editable = ['is_bool']

class Car_modelAdmin(admin.ModelAdmin):
    list_display = ('title','id')
    list_display_links = ['title']
    search_fields = ['title']
    # list_editable = ['is_bool']


admin.site.register(Car_model,Car_modelAdmin)
# admin.site.register(Aftosalon,AftosalonAdmin)
admin.site.register(Car,CarAdmin)
# admin.site.register(Categories,CategoriesAdmin)



