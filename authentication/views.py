from django.contrib import messages
from .forms import UserRegistrationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Users


# Create your views here.
def login(request):
    return render(request, 'authentication/login.html')


def registration(request):
    context = {}
    if request.method == 'POST':
        forms = UserRegistrationForm(request.POST)
        if forms.is_valid():
            email = request.POST.get('email')
            username = request.POST.get('username')
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            password = request.POST.get('password')
            phone = request.POST.get('phone')

            user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, password=password,
                                            username=username)
            user.save()
            details = Users(user_id=user.id, phone=phone)
            details.save()
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('auth:login')
        else:
            context['form'] = forms
            return render(request, 'authentication/registration.html', context)
    context['form'] = UserRegistrationForm
    return render(request, 'authentication/registration.html', context)
