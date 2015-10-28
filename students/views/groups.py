# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render

# Groups views
def groups_list(request):
    groups = [{'id':1, 'name':'МтМ-21', 'warden':u'Sylvester Stalone'},
              {'id':2, 'name':'МтМ-22', 'warden':u'Melissa Sagemiller'},
              {'id':3, 'name':'МтМ-23', 'warden':u'Бігун Олександр'}]
    context = {'groups':groups}
    return render(request, 'students/groups.html', context)


def groups_add(request):
    return HttpResponse("<h1>Group Add From</h1>")


def groups_edit(request, gid):
    return HttpResponse("<h1>Edit Group {0}</h1>".format(gid))


def groups_delete(request, gid):
    return HttpResponse("<h1>Delete Group {0}</h1>".format(gid))


