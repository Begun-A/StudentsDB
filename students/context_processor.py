# -*- coding: utf-8 -*-

from .utils import get_groups

def groups_proc(request):
    return {'GROUPS':get_groups(request)}