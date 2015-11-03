# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from ..models.student import Student
from ..models.group import Group
from datetime import datetime


# Create your views here.

# Students views
def students_list(request):
    students = Student.objects.all()

    # try to order students list
    group = request.GET.get('group')
    if group:
        students = students.filter(student_group=group)

    request.GET.order_by = 'first_name'
    order_by = request.GET.get('order_by', 'first_name')
    if order_by in ('id', 'first_name', 'last_name', 'ticket'):
        students = students.order_by(order_by)
        if request.GET.get('reverse', '') == '1':
            students = students.reverse()

    # #paginate students
    # paginator = Paginator(students,3)
    # page = request.GET.get('page')
    # try:
    #     students = paginator.page(page)
    # except PageNotAnInteger:
    #     students = paginator.page(1)
    # except EmptyPage:
    #     students = paginator.page(paginator.num_pages)

    # packing context
    context = {'students': students}
    return render(request, "students/students_list.html", context)


def students_add(request):
    # Was from posted?
    if request.method == 'POST':
        # Was form add button clicked?
        if request.POST.get('add_button') is not None:
            errors = {}
            data = {'midle_name': request.POST.get('midle_name'),
                    'notes': request.POST.get('notes')}
            # First_name Validation
            first_name = request.POST.get('first_name', '').strip()
            if not first_name:
                errors['first_name'] = u'Обов\'язкове поле'
            else:
                data['first_name'] = first_name
            # Last_name Validation
            last_name = request.POST.get('last_name', '').strip()
            if not last_name:
                errors['last_name'] = u'Обов\'язкове поле'
            else:
                data['last_name'] = last_name
            # Birthday Validation
            birthday = request.POST.get('birthday', '').strip()
            if not birthday:
                errors['birthday'] = u'Обов\'язкове поле'
            else:
                try:
                    datetime.strptime(birthday, '%Y-%m-%d')
                except Exception:
                    errors[
                        'birthday'] = u"Введіть коректний формат дати (напр. 1984-12-30)"
                else:
                    data['birthday'] = birthday
                data['birthday'] = birthday
            # Ticket Validation
            ticket = request.POST.get('ticket', '').strip()
            if not ticket:
                errors['ticket'] = u'Обов\'язкове поле'
            else:
                try:
                    int(ticket)
                except Exception:
                    errors['ticket'] = 'Повинно бути число'
                else:
                    data['ticket'] = ticket
            # Student_group Validation
            student_group = request.POST.get('student_group', '').strip()
            if not student_group:
                errors['student_group'] = u'Обов\'язкове поле'
            else:
                data['student_group'] = Group.objects.get(pk=student_group)
            # Photo Validation
            photo = request.FILES.get('photo')
            if photo:
                if photo.content_type.split('/')[0] != 'image':
                    errors['photo'] = 'Файл має бути image'
                elif photo._size > 2621440:
                    errors['photo'] = 'Файл занадто великий'
            else:
                data['photo'] = photo

            if not errors:
                # create student object
                student = Student(**data)
                student.save()
                messages.info(request, u'{0} {1} {2} був доданий у базу!'.format(
                    student.first_name, student.last_name,
                    student.midle_name))
                return HttpResponseRedirect(reverse('home'))
                # Was form cancel button clicked?
            else:
                messages.info(request, 'Будь-ласка, виправте наступні помилки')
                return render(request, 'students/students_add.html',
                              {'groups': Group.objects.all().order_by('title'),
                               'errors': errors})


        elif request.POST.get('calcel_button'):
            messages.info(request, u'Зміни скасовано' )
            return HttpResponseRedirect(reverse('home'))
    else:
        # initital from render
        return render(request, 'students/students_add.html',
                      {'groups': Group.objects.all().order_by('title')})


def students_edit(request, sid):
    return HttpResponse("<h1>Edit Student {0}</h1>".format(sid))


def students_delete(request, sid):
    return HttpResponse("<h1>Delete Student {0}</h1>".format(sid))
