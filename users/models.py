from django.db import models
from django.utils.translation import gettext_lazy as _

from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.

class MyUser(AbstractUser):
    major = models.CharField(_('major'), max_length=20, blank=True)
    is_student = models.BooleanField(
        _('student'),
        default=False,
        help_text=_('Designates whether the user is a student.'),
    )
    is_teacher = models.BooleanField(
        _('teacher'),
        default=False,
        help_text=_('Designates whether the user is a teacher.'),
    )
    is_admin = models.BooleanField(
        _('admin'),
        default=False,
        help_text=_('Designates whether the user is an admin.'),
    )


# TODO: set some fields to no blank

class Student(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    grade = models.IntegerField(blank=True)


class Teacher(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    seniority = models.IntegerField(blank=True)


@receiver(post_save, sender=MyUser)
def create_profile(sender, instance, created, **kwargs):
    if created and instance.is_student:
        Student.objects.create(user=instance)
    if created and instance.is_teacher:
        Teacher.objects.create(user=instance)


@receiver(post_save, sender=MyUser)
def save_profile(sender, instance, **kwargs):
    if instance.is_student:
        Student.objects.save()
    if instance.is_teacher:
        Teacher.objects.save()
