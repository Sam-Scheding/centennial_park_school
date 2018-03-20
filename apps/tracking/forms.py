from django import forms
from . import models
from datetime import time


class AddStudentForm(forms.ModelForm):

    class Meta:
        model = models.Student
        exclude = ['enrolled']

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


    class Meta:

        model = models.BehaviourTracking
        exclude = ('student',)
        
class EditStudentForm(forms.ModelForm):


    # TODO: Use this model form rather than manually creating it
    class Meta:

        model = models.Student
        fields = '__all__'
