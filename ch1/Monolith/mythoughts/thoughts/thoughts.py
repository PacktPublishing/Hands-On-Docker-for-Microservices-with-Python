from django.shortcuts import render, redirect
from .models import ThoughtModel, SessionModel


def get_username_from_session(request):
    cookie_session = request.COOKIES.get('session')
    try:
        session = SessionModel.objects.get(session=cookie_session)
    except SessionModel.DoesNotExist:
        return None

    return session.username


def list_thoughts(request):
    '''
    List the user's thoughts
    '''
    username = get_username_from_session(request)
    if not username:
        return redirect('login')

    user_thoughts = (ThoughtModel.objects
                     .filter(username=username)
                     .order_by('-timestamp'))

    context = {
        'thoughts': user_thoughts,
        'username': username,
    }
    return render(request, 'list_thoughts.html', context)


def new_thought(request):
    '''
    Create a new thought for the user
    '''
    username = get_username_from_session(request)
    if not username:
        return redirect('login')

    text = request.POST.get('text')

    if text:
        # Only store the thought if there's text in it
        new_thought = ThoughtModel(text=text, username=username)
        new_thought.save()

    return redirect('list-thoughts')
