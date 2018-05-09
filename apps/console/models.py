from django.db import models
from django.conf import settings


class Student(models.Model):

	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=40)
	class_name = models.CharField(max_length=10, choices=settings.CLASSES, default="C1")
	year = models.IntegerField(choices=settings.SCHOOL_YEARS)
	enroled = models.BooleanField(default=True)
	
	@property
	def full_name(self):
		return "{} {}".format(self.first_name, self.last_name)

	def __str__(self):
		return "{} {}".format(self.first_name, self.last_name)

	class Meta:
		pass

