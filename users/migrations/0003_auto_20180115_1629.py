# Generated by Django 2.0 on 2018-01-15 08:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20180115_1525'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='CourseList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='course')),
                ('year', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.CourseList'),
        ),
        migrations.AddField(
            model_name='course',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]