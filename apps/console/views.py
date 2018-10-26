from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.conf import settings
from django.http import HttpResponseRedirect
from . import models
from . import forms

class ConsoleView(generic.CreateView):

    template_name = 'console.html'
    success_url = '/console'
    model = models.Student
    fields = ['first_name', 'last_name', 'class_name', 'year']

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['students'] = models.Student.objects.filter(enroled=True)
        context['form'] = forms.AddStudentForm()
        return context


class DisenrolStudentView(generic.View):

    def post(self, request, *args, **kwargs):

        if not request.user.is_authenticated:
            return redirect('login')

        student_id = request.POST.get('student_id')
        student = models.Student.objects.get(id=student_id)
        student.enroled = False
        student.save()
        return redirect('console')


class EditStudentView(generic.UpdateView):

    template_name = 'edit_student.html'
    model = models.Student
    form_class = forms.EditStudentForm
    success_url = '/console'
