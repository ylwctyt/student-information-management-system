from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required

from . import settings

from django.contrib.admin.models import LogEntry


# Create your views here.

# @login_required(login_url=settings.LOGIN_URL)
@login_required()
def index(request):
    return redirect('/users/%s' % request.user.username)


@login_required(login_url=settings.LOGIN_URL)
def person_index(request, username):
    # if the user gets its own profile
    if request.user.username == username:
#        LogEntry.objects.get(id=1)
        return render(request, 'users/index2.html', {'username': username,
                                                     'name': request.user.last_name+request.user.first_name,
                                                     'email': request.user.email,
                                                     'major': request.user.student.major,})
#        return render(request, 'users/index.html', {'username': username})
    # if the user gets another user's profile
    else:
        return HttpResponse('Hello, ' + request.user.username + '. You\'re looking at ' + username + '\'s website.')
#        return render(request, 'users/index.html')
