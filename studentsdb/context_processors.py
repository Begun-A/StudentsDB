# -*- coding: utf-8 -*-

def students_proc(request):
    PORTAL_URL = 'http://' + request.get_host()
    return {'PORTAL_URL': PORTAL_URL}