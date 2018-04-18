from datetime import datetime
from collections import defaultdict
from django.shortcuts import render
from rest_framework import views
from rest_framework.response import Response
from django.core import serializers
from apps.behaviour.models import BehaviourTracking, Student
from pprint import pprint

NOT_AUTHED = 'User is not authenticated'

class StudentBehaviourTrackingAPIView(views.APIView):

    def get(self, request, *args, **kwargs):

        if not request.user.is_authenticated:
            return Response({'error': NOT_AUTHED})

        offset, day_num = 0, 0
        student_model = Student.objects.get(id=self.kwargs['student_id'])
        behaviour_tracking_set = BehaviourTracking.objects.filter(student=student_model, year=datetime.now().year).order_by('week', 'term', 'year')
        student = {
            'name': student_model.first_name + ' ' + student_model.last_name,
            'points': [],
            'id': student_model.id,
        }

        average_points = defaultdict(int)

        # TODO: numpy can probably do this in 2 lines 
        for bt in behaviour_tracking_set:
            day_num = (bt.week - 1) * 5
            tooltip = "B1: {}\nB2: {}".format(bt.b1, bt.b2)
            student['points'] += [
                [day_num, bt.monday_points, tooltip], 
                [day_num + 1, bt.tuesday_points, tooltip],
                [day_num + 2, bt.wednesday_points, tooltip],
                [day_num + 3, bt.thursday_points, tooltip],
                [day_num + 4, bt.friday_points, tooltip],
            ]
            average_points['monday'] += bt.monday_points if bt.monday_points != None else 0
            average_points['tuesday'] += bt.tuesday_points if bt.tuesday_points != None else 0
            average_points['wednesday'] += bt.wednesday_points if bt.wednesday_points != None else 0
            average_points['thursday'] += bt.thursday_points if bt.thursday_points != None else 0
            average_points['friday'] += bt.friday_points if bt.friday_points != None else 0

        student['num_days'] = day_num + 5
        weekday = student['num_days'] / 5
        student['average_monday_points'] = average_points['monday'] / weekday
        student['average_tuesday_points'] = average_points['tuesday'] / weekday
        student['average_wednesday_points'] = average_points['wednesday'] / weekday
        student['average_thursday_points'] = average_points['thursday'] / weekday
        student['average_friday_points'] = average_points['friday'] / weekday

        return Response(student)

class IsBehaviourTrackingUnique(views.APIView):

    def get(self, request, *args, **kwargs):

        if not request.user.is_authenticated:
            return Response({'error': NOT_AUTHED})
        behaviour_tracking = {
            'student': Student.objects.get(id=int(request.GET['student'])), 
            'year': int(request.GET['year']), 
            'week': int(request.GET['week']), 
            'term': int(request.GET['term']),
        }
        exists = BehaviourTracking.objects.filter(**behaviour_tracking).exists()
        return Response({'student': Student.objects.get(id=request.GET['student']).first_name, 'already_exists': exists, })


