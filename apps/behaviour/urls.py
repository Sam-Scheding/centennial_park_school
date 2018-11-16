from django.conf.urls import url, include
from django.urls import path

from . import views

urlpatterns = [
	url(r'^(?P<student_id>\d+)$', views.StudentTrackingView.as_view(), name='behaviour_student'),

]
