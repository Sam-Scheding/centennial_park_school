from django import forms


class ContactForm(forms.Form):

    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(
        required=True,
        widget=forms.Textarea
    )

    def clean(self):
        cleaned_data = super(ContactForm, self).clean()
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        email = cleaned_data.get('email')
        message = cleaned_data.get('message')
        if not first_name and not last_name and not email and not message:
            raise forms.ValidationError('Could Not Validate')
