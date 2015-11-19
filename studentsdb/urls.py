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

from students.views.students import StudentUpdateView, StudentDeleteView
from students.views.journals import JournalView


urlpatterns = patterns('students.views',
                       url(r'^admin/', include(admin.site.urls)),

                       # Students ,
                       url(r'^$', 'students.students_list', name='home'),
                       url(r'^students/add/$', 'students.students_add',
                           name='students_add'),
                       url(r'^students/(?P<pk>\d+)/edit/$',
                           StudentUpdateView.as_view(), name='students_edit'),
                       url(r'^students/(?P<pk>\d+)/delete/$',
                           StudentDeleteView.as_view(), name='students_delete'),

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
                       url(r'^journal/(?P<pk>\d+)?/?$', JournalView.as_view(),
                           name='journal'),
                       url(r'^journal/update/$', 'journals.journal_update',
                           name='journal_update'),

                       # Exam URLs
                       url(r'^exams/$', 'exams.exams_list', name='exam_list'),

                       # Resalts URLs
                       url(r'^resalts/$', 'resalts.resalts_list',
                           name='resalts_list'),

                       # Contact-admin URLs
                       url(r'^contacts/$', 'contact_admin.contact_admin',
                           name='contact_admin')
                       )

if DEBUG:
    urlpatterns += patterns('',
                            url(r'^media/(?P<path>.*)$',
                                'django.views.static.serve',
                                {'document_root': MEDIA_ROOT})
                            )
