from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader, RequestContext
# Create your views here.

# Students views
def students_list(request):
    return render(request, "students/students_list.html", {})

def students_add(request):
    return HttpResponse("<h1>Student Add From</h1>")

def students_edit(request, sid):
    return HttpResponse("<h1>Edit Student {0}</h1>".format(sid))

def students_delete(request, sid):
    return HttpResponse("<h1>Delete Student {0}</h1>".format(sid))

# Groups views
def groups_list(request):
    return HttpResponse("<h1>Groups list</h1>")

def groups_add(request):
    return HttpResponse("<h1>Group Add From</h1>")

def groups_edit(request, gid):
    return HttpResponse("<h1>Edit Group {0}</h1>".format(gid))

def groups_delete(request, gid):
    return HttpResponse("<h1>Delete Group {0}</h1>".format(gid))


# Journal views

def journal_all(request):
    return HttpResponse("<h1>Journal all</h1>")

def journal_students(request, jid):
    return HttpResponse("<h1>Journal Student {0}</h1>".format(jid))

def journal_update(request):
    return HttpResponse("<h1>Journal Update</h1>")