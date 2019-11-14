from django.shortcuts import render

from .models import ThoughtModel
from .thoughts import get_username_from_session


def search(request):
    username = get_username_from_session(request)
    search_param = request.GET.get('search')

    results = (ThoughtModel.objects
               .filter(text__icontains=search_param)
               .order_by('-timestamp'))

    context = {
        'thoughts': results,
        'username': username,
    }
    return render(request, 'search.html', context)
