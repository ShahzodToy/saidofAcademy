# Generated by Django 4.2 on 2024-10-08 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course_app', '0015_remove_mentor_workplace_mentorwork_mentor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mentorwork',
            name='mentor',
        ),
    ]
