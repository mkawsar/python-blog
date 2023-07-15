from django.urls import path
from .views import *

app_name = 'auth'

urlpatterns = [
    path('', login, name='login'),
    path('registration', registration, name='registration')
]
