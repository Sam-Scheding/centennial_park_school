from django.conf.urls import url, include

from . import views

urlpatterns = [
    # url(r'^behaviour_tracking/$', views.BehaviourTrackingAPIView.as_view()),
    url(r'^behaviour_tracking/(?P<student_id>\d*$)', views.StudentBehaviourTrackingAPIView.as_view()),
    url(r'^behaviour_tracking/is_unique/', views.IsBehaviourTrackingUnique.as_view()),
]
