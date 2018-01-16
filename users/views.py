from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required

from django.utils.translation import gettext as _

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


# TODO:list the course

@login_required(login_url=settings.LOGIN_URL)
def profile(request, username):
    # if the user gets its own profile
    if request.user.username == username:

        # my profile

        # basic profile tuple
        base_show_tuple = (_('basic information'),
                           ((_('username'), username),
                            (_('name'), request.user.last_name + request.user.first_name),
                            (_('email'), request.user.email),
                            (_('major'), request.user.major)),)
        # student profile tuple
        student_show_tuple = (_('student information'),
                              ((_('grade'), request.user.student.grade),),)
        # course tuple
        course_query_list = request.user.course_set.all()
        course_info_list = list(course_query_list.values_list('course__name', 'course__year', 'course__semester'))
        course_show_tuple = (_('course information'), course_info_list,)

        # professional experience

        intern_query_list = request.user.intern_set.all()
        # language
        intern_ln18_list = list(intern_query_list.values_list('is_zh', 'company_zh', 'company_en', ))
        intern_coname_list = tuple(map(lambda x: x[1] if x[0] else x[2], intern_ln18_list))
        # elements
        intern_elmt_list = list(intern_query_list.values_list('position', 'st_time', 'ed_time', 'contribution'))
        intern_titl_list = ['position', 'start time', 'end time', 'contribution', ]
        intern_info_list = tuple(map(lambda x: tuple(zip(intern_titl_list, x)), intern_elmt_list))
        # zip together
        intern_info_tuple = tuple(zip(intern_coname_list, intern_info_list))

        # make lists for passing the parameters

        lists = [{'name': _('my profile'), 'items': (base_show_tuple, student_show_tuple, course_show_tuple), },
                 {'name': _('professional experience'), 'items': intern_info_tuple}]

        return render(request, 'users/profile.html', {'username': username, 'lists': lists})
    else:
        return HttpResponse('Hello, ' + request.user.username + '. You\'re looking at ' + username + '\'s website.')
#        return render(request, 'users/index.html')
