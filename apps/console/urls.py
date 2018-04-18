from django.conf.urls import url, include
from django.urls import path

from . import views

urlpatterns = [
    url(r'^$', views.ConsoleView.as_view(), name='console'),
    url(r'^students/disenrol/(?P<student_id>\d+)', views.DisenrolStudentView.as_view() , name='disenrol_student'),
	url(r'^students/edit/(?P<pk>\d+)', views.EditStudentView.as_view(), name='edit_student'),
	url(r'^students/add/$', views.AddStudentView.as_view(), name='add_student'),
]
