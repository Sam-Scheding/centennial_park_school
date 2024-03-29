from django import forms
from . import models
from datetime import time



class StudentBehaviourTrackingForm(forms.ModelForm):

    def __init__(self, active_student=None, *args, **kwargs):
        super(StudentBehaviourTrackingForm, self ).__init__(*args, **kwargs)
        points_dict = {'class': 'weekday_points', 'min': 0, 'max': 100 }
        arrived_dict = { 'class': 'not_required' }


        for field in self.fields.values():
            field.widget.attrs['form'] = 'behaviour_tracking_form'
            field.widget.attrs['class'] = 'form_field'
            field.required = False

        self.fields['monday_points'].widget.attrs.update(points_dict)
        self.fields['tuesday_points'].widget.attrs.update(points_dict)
        self.fields['wednesday_points'].widget.attrs.update(points_dict)
        self.fields['thursday_points'].widget.attrs.update(points_dict)
        self.fields['friday_points'].widget.attrs.update(points_dict)
        self.fields['monday_arrived'].widget.attrs.update(arrived_dict)
        self.fields['tuesday_arrived'].widget.attrs.update(arrived_dict)
        self.fields['wednesday_arrived'].widget.attrs.update(arrived_dict)
        self.fields['thursday_arrived'].widget.attrs.update(arrived_dict)
        self.fields['friday_arrived'].widget.attrs.update(arrived_dict)

        # Remove ------ from choices
        self.fields['year'].choices = self.fields['year'].choices[1:]
        self.fields['term'].choices = self.fields['term'].choices[1:]

    # def clean_monday_arrived(self):
    #     if self.data['monday_arrived'] == '':
    #         return None
    # def clean_tuesday_arrived(self):
    #     if self.data['tuesday_arrived'] == '':
    #         return None
    # def clean_wednesday_arrived(self):
    #     if self.data['wednesday_arrived'] == '':
    #         return None
    # def clean_thursday_arrived(self):
    #     if self.data['thursday_arrived'] == '':
    #         return None
    # def clean_friday_arrived(self):
    #     if self.data['friday_arrived'] == '':
    #         return None

    class Meta:

        model = models.BehaviourTracking
        exclude = ('student',)
