# -*- coding: utf-8 -*-

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models.group import Group

def paginate(objects, size, request, context, var_name='object_list'):
    """Paginate objects provided by view.
    This function takes:
        * list of elements;
        * number of objects per page;
        * request object to get url parameters from;
        * context to set new variables into;
        * var_name - variable name for list of objects.
    It returns updated context object.
    """
    # apply pagination
    paginator = Paginator(objects, size)

    # try to get page number from request
    page = request.GET.get('page', '1')
    try:
        object_list = paginator.page(page)
    except PageNotAnInteger:
        # if page is not an integer, deliver first page
        object_list = paginator.page(1)
    except EmptyPage:
        # if page is out of range
        # deliver last page
        object_list = paginator.page(paginator.num_pages)
    # set variable into context
    context[var_name] = object_list
    context['is_paginated'] = object_list.has_other_pages()
    context['page_obj'] = object_list
    context['paginator'] = paginator

    return context


def get_groups(request):
    """Return list of existing groups"""

    # deferred import of Group model to avoid cycled imports


    # get current selected group
    cur_group = get_cur_group(request)

    groups = []
    for group in Group.objects.all().order_by('title'):
        groups.append({
            'id': group.id,
            'title': group.title,
            'leader': group.leader and '{0} {1}'.format(group.leader.first_name,
                                                     group.leader.last_name) or None,
            'selected': cur_group and cur_group.id == group.id and True or False
        })
    return groups

def get_cur_group(request):
    """Return curently selected group or None"""

    #we remember selected group in COOKIE
    pk = request.COOKIES.get('current_group')

    if pk:
        from .models.group import Group
        try:
            group = Group.objects.get(id=pk)
        except Group.DoesNotExist:
            return None
        else:
            return group
    return None

