# -*- coding: utf-8 -*-

from django.contrib import admin
from django.core.urlresolvers import reverse
from django.forms import ValidationError, ModelForm
from .models.group import Group
from .models.student import Student
from .models.monthjournal import MonthJournal
from .models.exam import Exam
from .models.resalt import Resalt


class StudentFormAdmin(ModelForm):
    def clean_student_group(self):
        group = Group.objects.filter(leader=self.instance)
        print self.instance
        if len(group) > 0 and self.cleaned_data['student_group'] != group[0]:
            raise ValidationError(u'Студент є старостою іншої групи.',
                                  code='invalid')
        return self.cleaned_data['student_group']


class StudentAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name', 'ticket', 'student_group']
    list_display_links = ['last_name', 'first_name']
    list_editable = ['student_group']
    ordering = ['last_name']
    list_filter = ['student_group']
    list_per_page = 10
    search_fields = ['last_name', 'first_name', 'midle_name', 'ticket', 'notes']
    form = StudentFormAdmin

    def view_on_site(self, obj):
        return reverse('students_edit', kwargs={'pk': obj.id})

# Register your models here.
models_list = [Group, MonthJournal, Exam, Resalt]
admin.site.register(models_list)
admin.site.register(Student, StudentAdmin)
