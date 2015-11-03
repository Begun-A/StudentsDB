"""studentsdb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home'
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url, patterns
from django.contrib import admin
from .settings import MEDIA_ROOT, DEBUG

urlpatterns = patterns('students.views',
                       url(r'^admin/', include(admin.site.urls)),

                       # Students ,
                       url(r'^$', 'students.students_list', name='home'),
                       url(r'^students/add/$', 'students.students_add',
                           name='students_add'),
                       url(r'^students/(?P<sid>\d+)/edit/$',
                           'students.students_edit', name='students_edit'),
                       url(r'^students/(?P<sid>\d+)/delete/$',
                           'students.students_delete', name='students_delete'),

                       # Groups URLs
                       url(r'^groups$', 'groups.groups_list',
                           name='groups_list'),
                       url(r'^groups/add/$', 'groups.groups_add',
                           name='groups_add'),
                       url(r'^groups/(?P<sid>\d+)/edit/$', 'groups.groups_edit',
                           name='groups_edit'),
                       url(r'^groups/(?P<sid>\d+)/delete/$',
                           'groups.groups_delete', name='groups_delete'),

                       # Journal URLs
                       url(r'^journal$', 'journal.journal_all',
                           name='journal_all'),
                       url(r'^journal/(?P<jid>\d+)$',
                           'journal.journal_students', name='journal_students'),
                       url(r'^journal/update/$', 'journal.journal_update',
                           name='journal_update'),

                       # Exam URLs
                       url(r'^exams$', 'exams.exams_list', name='exam_list'),

                       # Resalts URLs
                       url(r'^resalts$', 'resalts.resalts_list',
                           name='resalts_list')
                       )

if DEBUG:
    urlpatterns += patterns('',
                            url(r'^media/(?P<path>.*)$',
                                'django.views.static.serve',
                                {'document_root': MEDIA_ROOT})
                            )
