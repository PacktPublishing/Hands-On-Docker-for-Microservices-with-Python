from django.urls import path
from . import login, thoughts

urlpatterns = [
    path('', login.login, name='index'),
    path('login/', login.login, name='login'),
    path('thoughts/', thoughts.list_thoughts, name='list-thoughts'),
    path('thoughts/new', thoughts.new_thought, name='new-thought'),
]
