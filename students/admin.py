from django.contrib import admin
from .models import Student, Group

# Register your models here.
models_list = [Student, Group]
admin.site.register(models_list)