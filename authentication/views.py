from django.contrib import messages
from django.shortcuts import render
from .forms import UserRegistrationForm


# Create your views here.
def loginView(request):
    return render(request, 'authentication/login.html')

def registration(request):
    form = UserRegistrationForm
    return render(request, 'authentication/registration.html', {'form': form})