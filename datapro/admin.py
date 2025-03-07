from django.contrib import admin

# Register your models here.

from .models import DataCareer, Category, Article

admin.site.register(DataCareer)
admin.site.register(Category)
admin.site.register(Article)

