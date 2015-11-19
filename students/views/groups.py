# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render

from ..models.group import Group
from ..utils import paginate, get_cur_group

# Groups views
def groups_list(request):
    group = get_cur_group(request)
    if group:
        groups = [group]
    else:
        groups = Group.objects.all()
        order_by=request.GET.get('order_by','title')
        if order_by in ('title', 'id', 'leader'):
            groups = groups.order_by(order_by)
            if request.GET.get('reverse','')== '1':
                groups = groups.reverse()
    context = paginate(groups, 3, request, {}, var_name='groups')
    return render(request, 'students/groups.html', context)


def groups_add(request):
    return HttpResponse("<h1>Group Add From</h1>")


def groups_edit(request, gid):
    return HttpResponse("<h1>Edit Group {0}</h1>".format(gid))


def groups_delete(request, gid):
    return HttpResponse("<h1>Delete Group {0}</h1>".format(gid))


