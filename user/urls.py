from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^registration/complete/', views.registration_complete, name='user_registration_complete'),
    url(r'^registration/closed/', views.registration_closed, name='user_registration_closed'),
    url(r'^registration/', views.registration, name='user_registration'),
]