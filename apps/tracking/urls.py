from django.conf.urls import url, include
from django.urls import path

from . import views

urlpatterns = [
    url(r'^$', views.ConsoleView.as_view(), name='console'),
	url(r'^behaviour_tracking/(?P<student_id>\d+)$', views.StudentTrackingView.as_view(), name='student_behaviour_tracking'),
    url(r'^disenroll/', views.DisenrollStudentView.as_view() , name='disenroll_student'),
	url(r'^wios/(?P<student_id>\d*)', views.WorkItOutsView.as_view(), name='workitouts'),
	url(r'^edit_student/(?P<student_id>\d*)', views.EditStudentView.as_view(), name='edit_student'),
]