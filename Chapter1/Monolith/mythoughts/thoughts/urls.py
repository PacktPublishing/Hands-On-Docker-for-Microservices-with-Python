from django.urls import path
from . import login

urlpatterns = [
    path('', login.login, name='index'),
]
