# Generated by Django 4.2 on 2024-10-09 05:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course_app', '0021_rename_mentorachievment_mentorachievement_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coursedetail',
            name='module_course',
        ),
        migrations.AddField(
            model_name='module',
            name='course_module',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='module', to='course_app.coursedetail'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='forwhomcourse',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='for_Whom', to='course_app.course'),
        ),
    ]