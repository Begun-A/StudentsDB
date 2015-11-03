from django.contrib import admin
from .models.group import Group
from .models.student import Student
from .models.journal import Journal
from .models.exam import Exam
from .models.resalt import Resalt

# Register your models here.
models_list = [Student, Group, Journal, Exam, Resalt]
admin.site.register(models_list)