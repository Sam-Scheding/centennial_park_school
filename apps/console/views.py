from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.conf import settings
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from apps.console.models import Student
from apps.behaviour.models import BehaviourTracking
from apps.console import forms
from django.http import HttpResponse, HttpResponseNotFound
from django.contrib.auth.mixins import LoginRequiredMixin

from apps.console.reports import StudentReport

# from django.core.files.storage import FileSystemStorage

class ConsoleView(LoginRequiredMixin, generic.CreateView):

    template_name = 'console.html'
    success_url = reverse_lazy('students:overview')
    model = Student
    fields = ['first_name', 'last_name', 'class_name', 'year']

    def students(self):
        return Student.objects.filter(enroled=True)

class DisenrolStudentView(LoginRequiredMixin, generic.View):

    def post(self, request, *args, **kwargs):

        if not request.user.is_authenticated:
            return redirect('login')

        student_id = request.POST.get('student_id')
        student = Student.objects.get(id=student_id)
        student.enroled = False
        student.save()
        return redirect('students:overview')


class EditStudentView(LoginRequiredMixin, generic.UpdateView):

    template_name = 'edit_student.html'
    model =  Student
    form_class = forms.EditStudentForm
    success_url = reverse_lazy('students:overview')

class DownloadStudentReportView(LoginRequiredMixin, generic.View):

    success_url = reverse_lazy('students:overview')


    def get(self, request, *args, **kwargs):

        # Check that the request is valid
        if 'pk' not in kwargs:
            return redirect(self.success_url)

        student = Student.objects.get(**kwargs)
        points = BehaviourTracking.objects.filter(student=student).order_by('year', 'term', 'week')

        filename = '{}.pdf'.format('report')

        # write the report for the requested student
        report = StudentReport(student, points)
        pdf = report.generate()
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename="{}"'.format(filename)
        # response['Content-Disposition'] = 'attachment; filename="report.pdf"'  # Add the report as an attachment to the HTTP Response
        return response


        doc = SimpleDocTemplate(
                buffer,
                rightMargin=72,
                leftMargin=72,
                topMargin=30,
                bottomMargin=72,
                pagesize=self.pageSize)
        styles = getSampleStyleSheet()
        # create document
        data = []
        data.append(Paragraph(title, styles['Title']))
        # create other flowables
        doc.build(data)
        pdf = self.buffer.getvalue()
        buffer.close()
        return pdf
