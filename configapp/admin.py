from django.contrib import admin
from .models import *


class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('title','id')
    list_display_links = ['title']
    search_fields = ['title']
    # list_editable = ['is_bool']


admin.site.register(News)
admin.site.register(Aftosalon)
admin.site.register(Car)
admin.site.register(Categories,CategoriesAdmin)

