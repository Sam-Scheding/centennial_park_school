from django.conf.urls import url, include
from django.urls import path

from apps.console import views

app_name = 'students'

urlpatterns = [
    url(r'^$', views.ConsoleView.as_view(), name='overview'),
    url(r'^students/disenrol/(?P<student_id>\d+)', views.DisenrolStudentView.as_view() , name='disenrol'),
	url(r'^students/edit/(?P<pk>\d+)', views.EditStudentView.as_view(), name='edit'),
	# url(r'^students/add/$', views.AddStudentView.as_view(), name='add_student'),
]
