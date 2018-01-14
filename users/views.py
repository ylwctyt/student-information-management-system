from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required

from . import settings

from django.contrib.admin.models import LogEntry


# Create your views here.

@login_required(login_url=settings.LOGIN_URL)
def index(request):
    return redirect('/users/%s' % request.user.username)


@login_required(login_url=settings.LOGIN_URL)
def person_index(request, username):
    return render(request, 'users/person_index.html', {'username': username,
                                                       'name': request.user.last_name + request.user.first_name, })


@login_required(login_url=settings.LOGIN_URL)
def profile(request, username):
    # if the user gets its own profile
    if request.user.username == username:
        return render(request, 'users/profile.html', {'username': username,
                                                      'name': request.user.last_name + request.user.first_name,
                                                      'email': request.user.email,
                                                      'major': request.user.major,
                                                      'grade': request.user.student.grade})
    else:
        return HttpResponse('Hello, ' + request.user.username + '. You\'re looking at ' + username + '\'s website.')
#        return render(request, 'users/index.html')
