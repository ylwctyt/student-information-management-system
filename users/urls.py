from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='users.views.index'),
    path('<str:username>/', views.person_index, name='users.views.person_index'),
    path('<str:username>/profile', views.profile, name='users.views.profile'),
]