# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from ..models import Student

# Create your views here.

# Students views
def students_list(request):

    students = Student.objects.all()

    # try to order students list
    request.GET.order_by = 'first_name'
    order_by = request.GET.get('order_by','first_name')
    if order_by in ('id', 'first_name', 'last_name', 'ticket'):
        students = students.order_by(order_by)
        if request.GET.get('reverse', '')=='1':
            students = students.reverse()

    #paginate students
    paginator = Paginator(students,3)
    page = request.GET.get('page')
    try:
        students = paginator.page(page)
    except PageNotAnInteger:
        students = paginator.page(1)
    except EmptyPage:
        students = paginator.page(paginator.num_pages)
    #packing context
    context = {'students' : students}
    return render(request, "students/students_list.html", context)


def students_add(request):
    return HttpResponse("<h1>Student Add From</h1>")


def students_edit(request, sid):
    return HttpResponse("<h1>Edit Student {0}</h1>".format(sid))


def students_delete(request, sid):
    return HttpResponse("<h1>Delete Student {0}</h1>".format(sid))

