from django import forms
from django.forms import ValidationError


class UserRegistrationForm(forms.Form):
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)
    email = forms.CharField(max_length=100, required=True)
    password = forms.CharField(max_length=16, required=True, min_length=6)
