from django.db import models
from django.conf import settings


class StaffMembers(models.Model):

    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100, help_text="e.g. Art Therapist, Sports Coordinator, etc")
    title = models.CharField(max_length=100, choices=settings.STAFF_TITLES, default=settings.STAFF_TITLES[0])
    image = models.ImageField(blank=True)
    blurb = models.TextField(blank=True, default="")

    class Meta:

        app_label = 'staff'
        verbose_name = "Staff Member"
        verbose_name_plural = "Staff Members"

    @property
    def first_name(self):
        return self.name.split(" ")[0]

    def __str__(self):
        return "{} - {}".format(self.name, self.title)

