# Generated by Django 4.2 on 2024-10-08 13:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course_app', '0017_mentorwork_mentor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='forwhomcourse',
            name='course',
        ),
    ]