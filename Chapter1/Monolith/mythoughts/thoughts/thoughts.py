from django.shortcuts import render, redirect
from .models import ThoughtModel

user = 'bruce'


def list_thoughts(request):
    '''
    List the user's thoughts
    '''
    user_thoughts = (ThoughtModel.objects
                     .order_by('-timestamp'))

    context = {
        'thoughts': user_thoughts,
    }
    return render(request, 'list_thoughts.html', context)


def new_thought(request):
    '''
    Create a new thought for the user
    '''

    text = request.POST.get('text')
    user = 'bruce'

    if text:
        # Only store the thought if there's text in it
        new_thought = ThoughtModel(text=text, username=user)
        new_thought.save()

    return redirect('list-thoughts')
