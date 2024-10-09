# Generated by Django 4.2 on 2024-10-08 12:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course_app', '0014_mentor_mentorwork_rename_ordercourse_contact_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mentor',
            name='workPlace',
        ),
        migrations.AddField(
            model_name='mentorwork',
            name='mentor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='course_app.mentor'),
            preserve_default=False,
        ),
    ]