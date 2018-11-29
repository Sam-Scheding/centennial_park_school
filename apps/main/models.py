import re
from django.db import models
from django.conf import settings
import datetime


class Newsletter(models.Model):

    file_obj = models.FileField(upload_to='newsletters')
    year = models.IntegerField(choices=settings.YEAR_CHOICES, default=datetime.datetime.now().year)
    term = models.CharField(max_length=10, choices=settings.TERMS, default="Term 1")

    def __str__(self):
        return str(self.file_obj)

    @property
    def name(self):
        name = re.sub("newsletters/", '', str(self.file_obj))
        name = re.sub("_", " ", name)
        print(name)
        return str(name)

    class Meta:

        verbose_name = "Newsletter"
        verbose_name_plural = "Newsletters"


class ASR(models.Model):

    file_obj = models.FileField(upload_to='ASR')
    year = models.IntegerField(choices=settings.YEAR_CHOICES, default=datetime.datetime.now().year)

    def __str__(self):
        return str(self.file_obj)

    @property
    def name(self):
        name = re.sub("newsletters/", '', str(self.file_obj))
        name = re.sub("_", " ", name)
        print(name)
        return str(name)

    class Meta:

        verbose_name = "Annual School Report"
        verbose_name_plural = "Annual School Reports"

class Publication(models.Model):

    file_obj = models.FileField(upload_to='publications')
    name = models.CharField(max_length=256)
    class Meta:

        verbose_name = "publication"

class Event(models.Model):

    date = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=512)
    body = models.TextField(null=True, blank=True)
    permission_slip = models.FileField(upload_to='permission_slips', default=None, null=True, blank=True)

    @property
    def date_day(self):

        return self.date.strftime('%d')

    @property
    def date_month(self):

        return self.date.strftime('%B')

    def __str__(self):
        return str(self.date) + ": " + self.title

    class Meta:

        verbose_name = "event"
        verbose_name_plural = "events"


class Testimonial(models.Model):

    name = models.CharField(max_length=128)
    text = models.TextField()

    class Meta:

        verbose_name = "testimonial"
        verbose_name_plural = "testimonials"


class Subscriber(models.Model):

    email = models.EmailField()

    class Meta:

        verbose_name = "subscriber"
        verbose_name_plural = "subscribers"

    def __str__(self):
        return str(self.email)
