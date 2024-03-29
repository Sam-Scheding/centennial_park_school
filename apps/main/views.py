from django.shortcuts import render, redirect
from django.views import generic
from django.conf import settings
from . import models
import datetime

APPNAME = 'main'


class HomeView(generic.TemplateView):

    template_name = 'index.html'

    def num_enrolments(self):
        return settings.ENROLMENT_CAPACITY

    def events(self):

        start_date = datetime.date.today()
        end_date = start_date + datetime.timedelta(365 * 5)  # Show events for the next 5 years
        return models.Event.objects.order_by('date').filter(date__range=(start_date, end_date))[0:3]

class AboutView(generic.TemplateView):

    template_name = 'about.html'

    def num_enrolments(self):
        return settings.ENROLMENT_CAPACITY

class PublicationsView(generic.TemplateView):

    template_name = 'publications.html'

    def newsletters(self):
        return models.Newsletter.objects.all().order_by('-year', '-term')[0:10]

    def asrs(self):
        return models.ASR.objects.all().order_by('-year')[0:5]

    def publications(self):
        pubs = models.Publication.objects.all().order_by('name')
        print("HERE:", pubs)
        return pubs

class PaymentsView(generic.View):

    url = 'https://quickweb.westpac.com.au/OnlinePaymentServlet?cd_community=DETSQW&cd_supplier_business=5516&cd_currency=AUD&headerBoxColour=%2339b7ff&headerBackgroundColour=%2339b7ff&navigationBarColour=%23ffffff&navigationBarBackgroundColour=%2339b7ff&pageBackgroundColour=%2339b7ff&schoolNameFontColour=%23000000&schoolMottoFontColour=%23000000&schoolNameFontSize=33px&cancelURL=http://www.centennial-s.schools.nsw.edu.au/'
    url = 'https://quickweb.westpac.com.au/OnlinePaymentServlet?cd_community=DETSQW&cd_supplier_business=5516&cd_currency=AUD&headerBoxColour=%2339b7ff&headerBackgroundColour=%2339b7ff&navigationBarColour=%23ffffff&navigationBarBackgroundColour=%2339b7ff&pageBackgroundColour=%2339b7ff&schoolNameFontColour=%23000000&schoolMottoFontColour=%23000000&schoolNameFontSize=33px'

    def get(self, request):
        return redirect(self.url)


class SubscribeView(generic.View):

    template_name = 'index.html'  # Still needs this so the user can be redirected back to thte homepage

    def get(self, request):

        email = request.GET.get('Enter Email')
        subscribed = None

        if not models.Subscriber.objects.filter(email=email).exists():
            models.Subscriber(email=email).save()
            subscribed = True
        else:
            subscribed = False

        return render(request, self.template_name, {  # TODO: Change this to redirect, so I can delete template_name
            'subscribed': subscribed,
        })
