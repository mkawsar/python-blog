from django import forms
from django.forms import ValidationError
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


class UserRegistrationForm(forms.Form):
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)
    email = forms.CharField(max_length=100, required=True)
    username = forms.CharField(max_length=15, min_length=6, required=True)
    password = forms.CharField(max_length=16, required=True, min_length=6)
    phone = forms.CharField(required=True)

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise ValidationError('Email already exists')
        return email

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise ValidationError('Username already exists')
        return username
