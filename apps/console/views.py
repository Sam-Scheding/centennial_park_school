from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.conf import settings
from . import models
from . import forms

class ConsoleView(generic.TemplateView):

    template_name = 'console.html'
    def get(self, request, *args, **kwargs):

        if not request.user.is_authenticated:
            return redirect('login')

        form = forms.AddStudentForm()
        d = { 'classes': settings.CLASSES, 'students': models.Student.objects.all(), 'form':form }
        return render(request, self.template_name, d)


class AddStudentView(generic.CreateView):

    form_class = forms.AddStudentForm
    success_url = '/console'

class DisenrolStudentView(generic.View):

    def post(self, request, *args, **kwargs):

        if not request.user.is_authenticated:
            return redirect('login')

        student_id = request.POST.get('student_id')
        student = models.Student.objects.get(id=student_id)
        student.enrolled = False
        student.save()
        return redirect('console')


class EditStudentView(generic.UpdateView):

    template_name = 'edit_student.html'
    model = models.Student
    form_class = forms.EditStudentForm
    success_url = '/console'
