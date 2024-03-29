from django.db import models
from django.conf import settings
from apps.console.models import Student
from datetime import time
# Create your models here.


class BehaviourTracking(models.Model):

	student = models.ForeignKey(Student, on_delete=models.CASCADE)
	week = models.IntegerField(choices=settings.WEEK_CHOICES)
	term = models.IntegerField(choices=settings.TERM_CHOICES)
	year = models.IntegerField(choices=settings.BT_YEAR_CHOICES)
	b1 = models.CharField(max_length=256, blank=True)
	b2 = models.CharField(max_length=256, blank=True)

	monday_points = models.IntegerField(blank=True, default=0)
	monday_attended = models.IntegerField(default=0, choices=settings.ATTENDANCE_OPTIONS)
	monday_arrived = models.TimeField(default=time(9, 00, 00), choices=settings.SCHOOL_TIMES, blank=True)

	tuesday_points = models.IntegerField(blank=True, default=0)
	tuesday_attended = models.IntegerField(default=0, choices=settings.ATTENDANCE_OPTIONS)
	tuesday_arrived = models.TimeField(default=time(9, 00, 00), choices=settings.SCHOOL_TIMES, blank=True)

	wednesday_points = models.IntegerField(blank=True, default=0)
	wednesday_attended = models.IntegerField(default=0, choices=settings.ATTENDANCE_OPTIONS)
	wednesday_arrived = models.TimeField(default=time(9, 00, 00), choices=settings.SCHOOL_TIMES, blank=True)

	thursday_points = models.IntegerField(blank=True, default=0)
	thursday_attended = models.IntegerField(default=0, choices=settings.ATTENDANCE_OPTIONS)
	thursday_arrived = models.TimeField(default=time(9, 00, 00), choices=settings.SCHOOL_TIMES, blank=True)

	friday_points = models.IntegerField(blank=True, default=0)
	friday_attended = models.IntegerField(default=0, choices=settings.ATTENDANCE_OPTIONS)
	friday_arrived = models.TimeField(default=time(9, 00, 00), choices=settings.SCHOOL_TIMES, blank=True)


	class Meta:
		db_table = 'tracking_behaviourtracking'

	def __str__(self):
		return "{}: {} - term: {}, week: {}".format(self.student, self.year, self.term, self.week)
