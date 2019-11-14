from django.shortcuts import render, redirect
from .models import UserModel, SessionModel


def login(request):
    context = {}
    if request.method == 'POST':
        # Get the data and try to log
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        try:
            user = UserModel.objects.get(username=username)
            session = user.login_user(password)

            # Set session
            response = redirect('index')
            response.set_cookie('session', session)
            return response

        except (UserModel.DoesNotExist, UserModel.IncorrectPassword):
            context = {
                'no_log': True,
            }

    return render(request, 'login.html', context)


def logout(request):
    # Delete the session
    cookie_session = request.COOKIES.get('session')
    if cookie_session:
        # Delete it from the DB
        try:
            session = SessionModel.objects.get(session=cookie_session)
            session.delete()
        except SessionModel.DoesNotExist:
            pass

    # Delete session cookie
    response = redirect('login')
    response.delete_cookie('session')
    return response
