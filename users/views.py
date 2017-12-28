from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from . import settings


# Create your views here.

@login_required(login_url=settings.LOGIN_URL)
def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    return redirect('/users/%s' % request.user.username)


@login_required(login_url=settings.LOGIN_URL)
def person_index(request, username):
    # if the user gets another user's profile
    if request.user.username == username:
        return HttpResponse('Hello, ' + username + '. You\'re at the your own website.')
    # if the user gets its own profile
    else:
        return HttpResponse('Hello, ' + request.user.username + '. You\'re looking at ' + username + '\'s website.')
