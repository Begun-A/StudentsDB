# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
# Journal views

def journal_all(request):
    return render(request, 'students/journal.html', {})


def journal_students(request, jid):
    return HttpResponse("<h1>Journal Student {0}</h1>".format(jid))


def journal_update(request):
    return HttpResponse("<h1>Journal Update</h1>")
