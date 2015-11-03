# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render
from ..models.group import Group

# Groups views
def groups_list(request):
    groups = Group.objects.all()

    order_by=request.GET.get('order_by','title')
    if order_by in ('title', 'id', 'leader'):
        groups = groups.order_by(order_by)
        if request.GET.get('reverse','')== '1':
            groups = groups.reverse()
    context = {'groups':groups}
    return render(request, 'students/groups.html', context)


def groups_add(request):
    return HttpResponse("<h1>Group Add From</h1>")


def groups_edit(request, gid):
    return HttpResponse("<h1>Edit Group {0}</h1>".format(gid))


def groups_delete(request, gid):
    return HttpResponse("<h1>Delete Group {0}</h1>".format(gid))


