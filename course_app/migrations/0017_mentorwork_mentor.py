# Generated by Django 4.2 on 2024-10-08 13:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course_app', '0016_remove_mentorwork_mentor'),
    ]

    operations = [
        migrations.AddField(
            model_name='mentorwork',
            name='mentor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='workplace', to='course_app.mentor'),
            preserve_default=False,
        ),
    ]