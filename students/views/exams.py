# -*- coding: utf-8 -*-

from django.http import HttpResponse
from ..models.exam import Exam

def exams_list(request):
    exams = Exam.objects.all()
    return HttpResponse(request,exams)