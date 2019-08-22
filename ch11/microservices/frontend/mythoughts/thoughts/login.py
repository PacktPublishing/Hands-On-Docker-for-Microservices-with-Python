from django.shortcuts import render, redirect
from django.conf import settings
import requests
import http.client


def login(request):
    context = {}
    if request.method == 'POST':
        # Get the data and try to log
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        login_url = settings.USER_BACKEND + '/api/login'
        data = {
            'username': username,
            'password': password,
        }
        result = requests.post(login_url, data)
        if result.status_code == http.client.OK:
            # Obtain session
            session = result.json()['Authorized']
            # Set session
            response = redirect('index')
            response.set_cookie('session', session)
            return response

        context = {
            'no_log': True,
        }

    return render(request, 'login.html', context)


def logout(request):
    # Delete session cookie
    response = redirect('login')
    response.delete_cookie('session')
    return response
