from django.core.mail import send_mail
from django.conf import settings
# from django.shortcuts import render
from django.views import generic
from .forms import ContactForm


class ContactView(generic.FormView):

    template_name = 'contact.html'
    form_class = ContactForm
    success_url = '/contact/'

    def form_valid(self, form):
        message = "{name} / {email} said: ".format(
            name=form.cleaned_data.get('name'),
            email=form.cleaned_data.get('email'))

        message += "\n\n{0}".format(form.cleaned_data.get('message'))

        send_mail(
            subject='School Website Contact Page',
            message=message,
            from_email=form.cleaned_data.get('email'),
            recipient_list=settings.CONTACT_EMAILS,
        )
        return super(ContactView, self).form_valid(form)
