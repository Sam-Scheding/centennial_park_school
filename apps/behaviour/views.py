from django.http import HttpResponseRedirect
from django.views import generic
from . import models
from . import forms


class StudentTrackingView(generic.CreateView):

    template_name = 'student_tracking.html'
    form_class = forms.StudentBehaviourTrackingForm

    def get_success_url(self, **kwargs):

        return "/tracking/behaviour/{}?term={}".format(self.kwargs['student_id'], self.kwargs.get('term', 2))

    def get_context_data(self, **kwargs):
        context = super(StudentTrackingView, self).get_context_data(**kwargs)
        student = models.Student.objects.get(id=int(self.kwargs['student_id']))
        active_term = 'term_{}'.format(self.request.GET.get('term'))
        context['student'] = student  # Student needs to be set so the API knows which student to load
        context[active_term] = 'active'
        return context

    # Prob better to redirect to an update view if the data is already entered
    def form_valid(self, form):

        # Delete duplicate behaviour tracking
        models.BehaviourTracking.objects.filter(
            year=int(form.cleaned_data['year']), 
            term=int(form.cleaned_data['term']), 
            week=int(form.cleaned_data['week']), 
            student=models.Student.objects.get(id=int(self.kwargs['student_id'])),
        ).delete()
        new_form = form.save(commit=False) # Incomplete form because student is excluded
        new_form.student_id = int(self.kwargs['student_id'])
        new_form.save()
        form.save_m2m()
        return HttpResponseRedirect(self.get_success_url())


