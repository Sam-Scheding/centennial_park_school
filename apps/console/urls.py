from django.conf.urls import url, include
from django.urls import path

from apps.console import views

app_name = 'students'

urlpatterns = [
    path('', views.ConsoleView.as_view(), name='overview'),
    path('students/disenrol/<int:pk>', views.DisenrolStudentView.as_view() , name='disenrol'),
	path('students/edit/<int:pk>', views.EditStudentView.as_view(), name='edit'),
    path('student/report/<int:pk>', views.DownloadStudentReportView.as_view(), name='download')
]
