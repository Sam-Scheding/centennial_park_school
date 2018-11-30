from django.core.mail import send_mail
from django.conf import settings
# from django.shortcuts import render
from django.views import generic
from .forms import ContactForm
from django.contrib import messages
from django.urls import reverse_lazy

import multitasking

class ContactView(generic.FormView):

    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact')



    def get_form_kwargs(self):
        kwargs = super(ContactView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def form_invalid(self, form):
        messages.error(self.request, 'Email Not Set. Make sure all fields are filled in.', extra_tags='danger')
        return super(ContactView, self).form_invalid(form)

    def form_valid(self, form):

        self.send(form)
        messages.success(self.request, 'Thank you for getting in touch.')
        return super(ContactView, self).form_valid(form)

    @multitasking.task  # This is a decorator that turns send() into a non-blocking method
    def send(self, form):

        name = "{} {}".format(form.cleaned_data.get('first_name'), form.cleaned_data.get('last_name'))
        reply_to = form.cleaned_data.get('email')
        message = "{} | {}\n\n{}".format(name, reply_to, form.cleaned_data.get('message'))

        send_mail(
            'School Website Contact Page',
            message,
            'Centennial Park School <sam.scheding1@det.nsw.edu.au>',
            recipient_list=settings.CONTACT_EMAILS,
            fail_silently=False,
        )
