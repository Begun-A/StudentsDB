# -*- coding: utf-8 -*-

from django import forms
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.mail import send_mail
from django.contrib import messages
from django.views.generic.edit import FormView

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from studentsdb.settings import ADMIN_EMAIL
# Contact admin Form

class ContactForm(forms.Form):

    def __init__(self, *args, **kwargs):
        # call original initializator
        super(ContactForm, self).__init__(*args, **kwargs)
        # this helper object allows us to customize form
        self.helper = FormHelper()
        # form tag attributes
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.form_action = reverse('contact_admin')
        # twitter bootstrap styles
        self.helper.help_text_inline = True
        self.helper.html5_required = True
        self.helper.label_class = 'col-sm-2 control-label'
        self.helper.field_class = 'col-sm-10'
        # form buttons
        self.helper.add_input(Submit('send_button', u'Надіслати'))

    from_email = forms.EmailField(
        label=u'Ваша Емейл Адресса'
    )

    subject = forms.CharField(
        label=u'Заголовок листа',
        max_length=128
    )

    message = forms.CharField(
        label=u'Повідомлення',
        max_length=2560,
        widget=forms.Textarea
    )

class ContactView(FormView):
    template_name = 'contact_form.html'
    form_class = ContactForm
    success_url = '/email_send/'

    def form_valid(self, form):
        subject = form.cleaned_data['subject']
        message = form.cleaned_data['message']
        from_email = form.cleaned_data['from_email']

        send_mail(subject, message, from_email, ['admin@studentsdb.com'])
        return super(ContactView, self).form_valid(form)


def contact_admin(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            from_email = form.cleaned_data['from_email']

            try:
                send_mail(subject, message, from_email, [ADMIN_EMAIL])
            except Exception:
                message = u'Під час відправки листа виникла непередбачувана пом' \
                          u'илка. Спробуйте скористатись даною формою пізніше.'+ unicode(Exception.message)
            else:
                message = u'Повідомлення успішно надіслане!'
            messages.info(request, message )
            return HttpResponseRedirect(reverse('contact_admin'))

    else :
        form = ContactForm()
    return render(request, 'contact_admin/form.html', {'form': form})
