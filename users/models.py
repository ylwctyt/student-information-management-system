from django.db import models
from django.utils.translation import gettext_lazy as _

from django.contrib import admin

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


# courseList

class CourseList(models.Model):
    SEMESTER = (('A', '秋'), ('S', '春'))

    name = models.CharField(_('course'), max_length=50)
    year = models.IntegerField()
    semester = models.CharField(max_length=1, choices=SEMESTER)


class Course(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    course = models.ForeignKey(CourseList, on_delete=models.CASCADE)

    def __str__(self):
        return self.course.name


@receiver(post_save, sender=MyUser)
def create_profile(sender, instance, created, **kwargs):
    if created and instance.is_student:
        Student.objects.create(user=instance, grade=2016)
    if created and instance.is_teacher:
        Teacher.objects.create(user=instance)


@receiver(post_save, sender=MyUser)
def save_profile(sender, instance, **kwargs):
    if instance.is_student:
        Student.objects.update_or_create(user=instance)
    if instance.is_teacher:
        Teacher.objects.update_or_create(user=instance)
