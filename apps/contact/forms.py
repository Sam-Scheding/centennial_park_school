from django import forms
from django.conf import settings
import urllib, json

class ContactForm(forms.Form):

    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(required=True, widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(ContactForm, self).__init__(*args, **kwargs)

    def clean(self):

        ca = self.request.POST["g-recaptcha-response"]
        url = "https://www.google.com/recaptcha/api/siteverify"
        params = {
            'secret': settings.RECAPTCHA_SECRET_KEY,
            'response': ca,
            'remoteip': self.get_client_ip(self.request)
        }
        args = urllib.parse.urlencode(params).encode("utf-8")
        response = urllib.request.urlopen(url, args)
        verify_rs = json.loads(response.read().decode('utf8'))
        status = verify_rs.get("success", False)

        if not status:
            raise forms.ValidationError(('Captcha Validation Failed.'), code='invalid')

        cleaned_data = super(ContactForm, self).clean()
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        email = cleaned_data.get('email')
        message = cleaned_data.get('message')
        if not first_name and not last_name and not email and not message:
            raise forms.ValidationError('Could Not Validate')

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip