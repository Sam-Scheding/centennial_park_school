from django.shortcuts import render
from django.views import generic
from apps.staff.models import StaffMembers


class StaffView(generic.TemplateView):

    template_name = 'staff.html'

    def exec_staff(self):
        return StaffMembers.objects.filter(title='Executive')

    def teaching_staff(self):
        return StaffMembers.objects.filter(title='Teaching')

    def non_teaching_staff(self):
        return StaffMembers.objects.filter(title='Non-Teaching')

    def other_staff(self):
        return StaffMembers.objects.filter(title='Other')
