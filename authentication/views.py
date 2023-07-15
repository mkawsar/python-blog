from django.contrib import messages
from django.shortcuts import render
from .forms import UserRegistrationForm
from django.http import HttpResponse


# Create your views here.
def login(request):
    return render(request, 'authentication/login.html')


def registration(request):
    context = {}
    if request.method == 'POST':
        forms = UserRegistrationForm(request.POST)
        if forms.is_valid():
            print(request.POST)
        else:
            context['form'] = forms
            return render(request, 'authentication/registration.html', context)
    context['form'] = UserRegistrationForm
    return render(request, 'authentication/registration.html', context)
