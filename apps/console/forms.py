from django import forms
from apps.console.models import Student

class AddStudentForm(forms.ModelForm):

    class Meta:
        model = Student
        exclude = ['enroled']
        
class EditStudentForm(forms.ModelForm):


    # TODO: Use this model form rather than manually creating it
    class Meta:

        model = Student
        fields = '__all__'
