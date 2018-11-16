from django.http import HttpResponseRedirect
from django.db.utils import IntegrityError
from django.views import generic
from django.conf import settings
from django.urls import reverse_lazy
from django.shortcuts import redirect
from . import models
from . import forms


class StudentTrackingView(generic.CreateView):

    template_name = 'student_tracking.html'
    form_class = forms.StudentBehaviourTrackingForm
    # fields = '__all__'

    def get_success_url(self, **kwargs):
        return "/tracking/behaviour/{}?term={}".format(self.kwargs['student_id'], self.kwargs.get('term', settings.CURRENT_TERM))

    # Prob better to redirect to an update view if the data is already entered
    def form_valid(self, form):
        # Delete duplicate behaviour tracking
        models.BehaviourTracking.objects.filter(
            year=int(form.cleaned_data.get('year', settings.CURRENT_YEAR)),
            term=int(form.cleaned_data.get('term', settings.CURRENT_TERM)),
            week=int(form.cleaned_data.get('week', 0)),
            student=models.Student.objects.get(id=int(self.kwargs['student_id'])),
        ).delete()
        try:
            new_form = form.save(commit=False) # Incomplete form because student is excluded
            new_form.student_id = int(self.kwargs['student_id'])
            new_form.save()
            form.save_m2m()
        except Exception as e:
            print("CAUGHT THIS:", e)
        print("HERE:", form.cleaned_data)
        return super().form_valid(form)

    # Student needs to be set so the API knows which student to load
    @property
    def student(self):
        student = models.Student.objects.get(id=int(self.kwargs['student_id']))
        return student


    @property
    def current_term(self):
        """
            If the user has clicked on a term tab to view that terms points, load make that the active term.
            otherwise, load the current term from settings
        """
        term = self.request.GET.get('term', self.request.POST.get('term', settings.CURRENT_TERM))
        return term
