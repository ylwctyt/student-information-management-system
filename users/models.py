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


# TODO:trans?

class Intern(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    is_zh = models.BooleanField(_('is_zh'), default='True')
    company_zh = models.CharField(_('company_zh'), max_length=80)
    company_en = models.CharField(_('company_zh'), max_length=150, blank=True)
    position = models.CharField(_('position'), max_length=10, blank=True, default='intern')
    st_time = models.DateField()
    ed_time = models.DateField()
    contribution = models.TextField()

    def __str__(self):
        if self.is_zh:
            return self.company_zh
        else:
            return self.company_en


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
