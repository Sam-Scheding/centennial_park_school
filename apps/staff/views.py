from django.shortcuts import render
from django.views.generic import TemplateView
from .import models


class StaffView(TemplateView):

    template_name = 'staff.html'

    def get(self, request):

        exec_staff = models.StaffMembers.objects.filter(title='Executive')
        teaching_staff = models.StaffMembers.objects.filter(title='Teaching')
        non_teaching_staff = models.StaffMembers.objects.filter(title='Non-Teaching')
        other_staff = models.StaffMembers.objects.filter(title='Other')

        return render(request, self.template_name, {
            'exec_staff': exec_staff,
            'teaching_staff': teaching_staff,
            'non_teaching_staff': non_teaching_staff,
            'other_staff': other_staff,

        })
