# -*- coding: utf-8 -*-

from calendar import monthrange, weekday, day_abbr
from datetime import datetime, date
from dateutil.relativedelta import relativedelta

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic import TemplateView
from django.core.urlresolvers import reverse

from ..models.student import Student
from ..models.monthjournal import MonthJournal
from ..utils import paginate, get_cur_group
# Journal views

class JournalView(TemplateView):
    template_name = 'students/journal.html'
    # get context data from TemplateView class
    def get_context_data(self, **kwargs):
        context = super(JournalView, self).get_context_data(**kwargs)

        # check if we need display some specific month
        if self.request.GET.get('month'):
            month = datetime.strptime(self.request.GET['month'],
                                      '%Y-%m-%d').date()
        else:
            # otherwise just displaying current month data
            today = datetime.today()
            month = date(today.year, today.month, 1)

        # calculate current, previous and next month details
        # we need this for month navigation element in template
        prev_month = month - relativedelta(months=1)
        next_month = month + relativedelta(months=1)
        context['prev_month'] = prev_month.strftime('%Y-%m-%d')
        context['next_month'] = next_month.strftime('%Y-%m-%d')
        context['year'] = month.year
        context['month_verbose'] = month.strftime('%B')
        # we'll use this variable in students pagination
        context['cur_month'] = month.strftime('%Y-%m-%d')
        # prepare variable for template generation
        # journal table header elements
        myear, mmonth = month.year, month.month
        number_of_days = monthrange(myear, mmonth)[1]
        context['month_header'] = [
            {'day': d, 'verbose': day_abbr[weekday(myear, mmonth, d)][:2]}
            for d in range(1, number_of_days + 1)]
        # get students from data base
        group = get_cur_group(self.request)
        if kwargs['pk']:
            queryset = [Student.objects.get(pk=kwargs['pk'])]
        elif group:
            queryset = Student.objects.filter(student_group=group).order_by(
                'last_name')
        else:
            queryset = Student.objects.all().order_by('last_name')
        # url for update students presence, for form post
        update_url = reverse('journal')
        # go over all students and colect data about presence
        # during selected month
        students = []
        for student in queryset:
            # try to get journal objecy by month selected
            # month and current student
            try:
                journal = MonthJournal.objects.get(student=student,
                                                   date=month)
            except Exception:
                journal = None

            days = []
            for day in range(1, number_of_days + 1):
                days.append({
                    'day': day,
                    'present': journal and getattr(journal,
                                                   'present_day_{0}'.format(
                                                       day), False) or False,
                    'date': date(myear, mmonth, day).strftime('%Y-%m-%d')
                })
            # prepare metadata for current student
            students.append({
                'fullname': u'{0} {1}'.format(student.last_name,
                                              student.first_name),
                'days': days,
                'id': student.id,
                'update_url': update_url,
            })

        context = paginate(students, 10, self.request, context,
                           var_name='students')
        return context

    def post(self, request, *args, **kwargs):

        # prepare student, date and present data
        data = request.POST
        current_date = datetime.strptime(data['date'], '%Y-%m-%d').date()
        month = date(current_date.year, current_date.month, 1)
        present = data['present'] and True or False
        student = Student.objects.get(pk=data['pk'])

        # get or create journal object for current given student and date
        journal = MonthJournal.objects.get_or_create(student=student,
                                                     date=month)[0]

        # set present on journal for given student and save resalt
        setattr(journal, 'present_day_{0}'.format(current_date.day), present)
        journal.save()

        # return success status
        return JsonResponse({'status': 'success'})


def journal_students(request, jid):
    return HttpResponse("<h1>Journal Student {0}</h1>".format(jid))


def journal_update(request):
    return HttpResponse("<h1>Journal Update</h1>")
