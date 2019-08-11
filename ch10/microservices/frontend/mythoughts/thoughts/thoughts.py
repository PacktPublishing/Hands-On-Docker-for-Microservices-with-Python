import requests
import http.client
from django.conf import settings
from django.shortcuts import render, redirect
from .token_validation import validate_token_header


def get_username_from_session(request):
    cookie_session = request.COOKIES.get('session')
    username = validate_token_header(cookie_session,
                                     settings.TOKENS_PUBLIC_KEY)
    if not username:
        return None

    return username


def list_thoughts(request):
    '''
    List the user's thoughts
    '''
    username = get_username_from_session(request)
    if not username:
        return redirect('login')

    url = settings.THOUGHTS_BACKEND + '/api/me/thoughts/'
    headers = {
        'Authorization': request.COOKIES.get('session'),
    }
    result = requests.get(url, headers=headers)
    if result.status_code != http.client.OK:
        return redirect('login')

    context = {
        'thoughts': result.json(),
        'username': username,
    }
    return render(request, 'list_thoughts.html', context)


def new_thought(request):
    '''
    Create a new thought for the user
    '''
    text = request.POST.get('text')

    # Only store the thought if there's text in it
    if text:
        new_url = settings.THOUGHTS_BACKEND + '/api/me/thoughts/'
        data = {
            'text': text
        }
        headers = {
            'Authorization': request.COOKIES.get('session'),
        }
        result = requests.post(new_url, data, headers=headers)
        if result.status_code != http.client.CREATED:
            return redirect('login')

    return redirect('list-thoughts')
