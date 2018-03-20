from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.views import generic
from django.conf import settings
from django.forms import formset_factory
from . import models
from . import forms

APP_NAME = 'tracking'

class ConsoleView(generic.TemplateView):

    template_name = 'console.html'
    def get(self, request, *args, **kwargs):

        if not request.user.is_authenticated:
            return redirect('login')

        form = forms.AddStudentForm()
        d = { 'classes': settings.CLASSES, 'students': models.Student.objects.all(), 'form':form }
        return render(request, self.template_name, d)

    def post(self, request, *args, **kwargs):

        if not request.user.is_authenticated:
            return redirect('login')

        student = models.Student.objects.create(
            first_name=request.POST.get('first_name'),
            last_name=request.POST.get('last_name'),
            class_name=request.POST.get('class_name'),
            year=request.POST.get('year'),
            enrolled=True
            )
        student.save()
        return redirect('console')

class DisenrollStudentView(generic.View):

    def post(self, request, *args, **kwargs):

        if not request.user.is_authenticated:
            return redirect('login')

        student_id = request.POST.get('student_id')
        student = models.Student.objects.get(id=student_id)
        student.enrolled = False
        student.save()
        return redirect('console')


# class BehaviourTrackingView(generic.CreateView):

#   template_name = 'behaviour_tracking.html'
#   form_class = forms.AddBehaviourTrackingForm

#   def get_success_url(self, **kwargs):
#       return "/tracking/behaviour_tracking/{}".format(self.request.POST.get('student', ''))



class StudentTrackingView(generic.CreateView):

    template_name = 'student_tracking.html'
    form_class = forms.StudentBehaviourTrackingForm

    def get_success_url(self, **kwargs):

        return "/tracking/behaviour_tracking/{}".format(self.kwargs['student_id'])

    def get_context_data(self, **kwargs):
        context = super(StudentTrackingView, self).get_context_data(**kwargs)
        student = models.Student.objects.get(id=int(self.kwargs['student_id']))
        context['student'] = student  # Student needs to be set so the API knows which student to load
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


class WorkItOutsView(generic.TemplateView):

    template_name = 'work_it_outs.html'
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        active_student = kwargs.get('student_id', None)
        form = forms.AddWorkItOutForm(active_student=active_student)
        d = { 'form': form, }

        return render(request, self.template_name, d)


    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')

        student = models.Student.objects.get(id=int(request.POST.get('student')))

        wio = models.WorkItOut.objects.create(
            student=student,
            date=request.POST.get('date'),
            wio_type=request.POST.get('wio_type'),
        )
        wio.save()
        return redirect('console')


class EditStudentView(generic.TemplateView):

    template_name = 'edit_student.html'
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')

        student_id = kwargs.get('student_id')
        student = models.Student.objects.get(id=student_id)
        form = forms.EditStudentForm(instance=student)
        d = { 'form': form, 'student': student, }
        return render(request, self.template_name, d)

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')

        student_id = kwargs.get('student_id')
        student = models.Student.objects.filter(id=int(student_id))
        if request.POST.get('enrolled') == 'on':
            enrolled = True
        else:
            enrolled = False
        student.update(
            first_name=request.POST.get('first_name'),
            last_name=request.POST.get('last_name'),
            year=request.POST.get('year'),
            class_name=request.POST.get('class_name'),
            enrolled=enrolled,
        )
        return redirect('console')


