# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.views.generic import ListView, UpdateView, DeleteView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.bootstrap import FormActions

from datetime import datetime

from ..models.student import Student
from ..models.group import Group
from ..utils import paginate, get_cur_group

# Create your views here.

# Students views
# class StudentView(ListView):
#     model = Student
#     context_object_name = 'students'
#     template_name = 'students/students_listCL.html'
#
#     def get_context_data(self, **kwargs):
#         context = super(StudentView,self).get_context_data(**kwargs)
#         context['show_logo'] = False
#         return context
#
#     def get_queryset(self):
#         qs = super(StudentView, self).get_queryset()
#         return qs.order_by('last_name')


def students_list(request):

    # try to order students list
    group = get_cur_group(request)
    if group:
        students = Student.objects.filter(student_group=group)
    else:
        students = Student.objects.all()

    request.GET.order_by = 'first_name'
    order_by = request.GET.get('order_by', 'first_name')
    if order_by in ('id', 'first_name', 'last_name', 'ticket'):
        students = students.order_by(order_by)
        if request.GET.get('reverse', '') == '1':
            students = students.reverse()

    # #paginate students
    # paginator = Paginator(students,3)
    # page = request.GET.get('page')
    # try:
    #     students = paginator.page(page)
    # except PageNotAnInteger:
    #     students = paginator.page(1)
    # except EmptyPage:
    #     students = paginator.page(paginator.num_pages)

    # packing context
    context = paginate(students, 5, request, {}, var_name='students')
    return render(request, "students/students_list.html", context)


def students_add(request):
    # Was from posted?
    form = StudentAddUpdateForm(request.POST or None)
    context = {'form': form, 'meta_title':'Студенти', 'title':'Додати Студентa'}
    if request.POST.get('cancel_button'):
        messages.info(request, u'Додавання студента відмінено!')
        return HttpResponseRedirect(reverse('home'))
    elif request.POST.get('add_button'):
        if form.is_valid():
            student = Student(**form.cleaned_data)
            student.save()
            messages.info(request,
                          u'{0} {1} {2} був доданий у базу!'.format(
                              form.cleaned_data['first_name'],
                              form.cleaned_data['last_name'],
                              form.cleaned_data['midle_name']))
            return HttpResponseRedirect(reverse('home'))
    return render(request, 'students/students_add_edit.html', context)



class StudentAddUpdateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(StudentAddUpdateForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        # set form tag attributes
        try:
            kwargs['instance'].id
        except KeyError:
            self.helper.form_action = reverse('students_add')
        else:
            self.helper.form_action = reverse('students_edit',
                                              kwargs={'pk': kwargs['instance'].id})
        self.helper.form_method = 'POST'
        self.helper.form_class = 'form-horizontal'

        # set form fields proprties
        self.helper.field_class = 'col-sm-12'
        self.helper.label_class = 'col-sm-2 control-label'
        self.helper.help_text_inline = True
        self.html5_required = True

        # add buttom
        self.helper.layout.append( FormActions(
            Submit('add_button', u'Зберегти', css_class='btn btn-primary'),
            Submit('cancel_button', u'Скасувати', css_class='btn btn-link')
        ))

    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'midle_name', 'photo', 'ticket',
                  'student_group', 'birthday', 'notes']


class StudentUpdateView(UpdateView):
    model = Student
    template_name = 'students/students_add_edit.html'
    form_class = StudentAddUpdateForm

    def get_success_url(self):
        return reverse('home')

    def get_context_data(self, **kwargs):
        context = super(StudentUpdateView, self).get_context_data(**kwargs)
        context['meta_title'] = 'Редагувати Студента'
        context['title'] = 'Редагувати Студента'
        return context

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            messages.info(request, u'Редагування студента відмінено!')
            return HttpResponseRedirect(reverse('home'))
        else:
            messages.info(request, u'Редагування успішно збережено!')
            return super(StudentUpdateView, self).post(request, *args, **kwargs)


class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'students/students_confirm_dele 1te.html'

    def get_context_data(self, **kwargs):
        context = super(StudentDeleteView, self).get_context_data(**kwargs)
        context['messages'] = 'Студента успішно видалено!'
        return context

    def get_success_url(self):
        return u'{0}?messages=Студента успішно видалено!'.format(reverse('home'))