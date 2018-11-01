from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.conf import settings
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from apps.console.models import Student
from apps.console import forms

class ConsoleView(generic.CreateView):

    template_name = 'console.html'
    success_url = reverse_lazy('students:overview')
    model = Student
    fields = ['first_name', 'last_name', 'class_name', 'year']

    def students(self):
        return Student.objects.filter(enroled=True)

class DisenrolStudentView(generic.View):

    def post(self, request, *args, **kwargs):

        if not request.user.is_authenticated:
            return redirect('login')

        student_id = request.POST.get('student_id')
        student = Student.objects.get(id=student_id)
        student.enroled = False
        student.save()
        return redirect('students:overview')


class EditStudentView(generic.UpdateView):

    template_name = 'edit_student.html'
    model =  Student
    form_class = forms.EditStudentForm
    success_url = reverse_lazy('students:overview')
