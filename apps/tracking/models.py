from django.db import models
from django.conf import settings
# Create your models here.

class Student(models.Model):

	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=40)
	class_name = models.CharField(max_length=10, choices=settings.CLASSES, default="C1")
	year = models.IntegerField(choices=settings.SCHOOL_YEARS)
	enrolled = models.BooleanField(default=False)
	
	@property
	def full_name(self):
		return "{} {}".format(self.first_name, self.last_name)

	def __str__(self):
		return "{} {}".format(self.first_name, self.last_name)
	
class BehaviourTracking(models.Model):

	student = models.ForeignKey(Student, on_delete=models.CASCADE)
	week = models.IntegerField(choices=settings.WEEK_CHOICES)
	term = models.IntegerField(choices=settings.TERM_CHOICES)
	year = models.IntegerField(choices=settings.BT_YEAR_CHOICES)
	b1 = models.CharField(max_length=256, blank=True)
	b2 = models.CharField(max_length=256, blank=True)

	monday_points = models.IntegerField(blank=True)
	monday_attended = models.IntegerField(default=0, choices=settings.ATTENDANCE_OPTIONS)
	monday_arrived = models.TimeField(default=settings.SCHOOL_TIMES[0], choices=settings.SCHOOL_TIMES)

	tuesday_points = models.IntegerField(blank=True)
	tuesday_attended = models.IntegerField(default=0, choices=settings.ATTENDANCE_OPTIONS)
	tuesday_arrived = models.TimeField(default=settings.SCHOOL_TIMES[0], choices=settings.SCHOOL_TIMES)

	wednesday_points = models.IntegerField(blank=True)
	wednesday_attended = models.IntegerField(default=0, choices=settings.ATTENDANCE_OPTIONS)
	wednesday_arrived = models.TimeField(default=settings.SCHOOL_TIMES[0], choices=settings.SCHOOL_TIMES)

	thursday_points = models.IntegerField(blank=True)
	thursday_attended = models.IntegerField(default=0, choices=settings.ATTENDANCE_OPTIONS)
	thursday_arrived = models.TimeField(default=settings.SCHOOL_TIMES[0], choices=settings.SCHOOL_TIMES)

	friday_points = models.IntegerField(blank=True)
	friday_attended = models.IntegerField(default=0, choices=settings.ATTENDANCE_OPTIONS)
	friday_arrived = models.TimeField(default=settings.SCHOOL_TIMES[0], choices=settings.SCHOOL_TIMES)

	def __str__(self):
		return "{}: {} - term: {}, week: {}".format(self.student, self.year, self.term, self.week)

