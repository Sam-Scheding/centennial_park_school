from django.conf.urls import url, include

from . import views

urlpatterns = [
    # url(r'^behaviour_tracking/$', views.BehaviourTrackingAPIView.as_view()),
    url(r'^behaviour/(?P<student_id>\d*$)', views.StudentBehaviourTrackingAPIView.as_view()),
    url(r'^behaviour/is_unique/', views.IsBehaviourTrackingUnique.as_view()),
    url(r'^student/exists/', views.IsStudentUnique.as_view()),
]
