# -*- coding: utf-8 -*-

from django.http import HttpResponse
from ..models.resalt import Resalt

def resalts_list(request):
    resalts = Resalt.objects.all()
    return HttpResponse()