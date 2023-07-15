from django.urls import path
from .views import *

app_name = 'auth'

urlpatterns = [
    path('', loginView, name='login'),
]
