# Generated by Django 4.2 on 2024-10-08 12:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course_app', '0013_remove_coursedetail_forwhom_forwhomcourse_course'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=125)),
                ('image', models.ImageField(upload_to='mentors')),
                ('experience', models.CharField(max_length=125)),
                ('position', models.CharField(max_length=125)),
                ('position_uz', models.CharField(max_length=125, null=True)),
                ('position_ru', models.CharField(max_length=125, null=True)),
                ('profession', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mentors', to='course_app.mentorprofession')),
            ],
            options={
                'verbose_name': 'Mentors',
            },
        ),
        migrations.CreateModel(
            name='MentorWork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='worked_place')),
            ],
            options={
                'verbose_name': 'MentorWorkPLace',
            },
        ),
        migrations.RenameModel(
            old_name='OrderCourse',
            new_name='Contact',
        ),
        migrations.RenameModel(
            old_name='PlanCourse',
            new_name='CoursePlan',
        ),
        migrations.RemoveField(
            model_name='mentors',
            name='profession',
        ),
        migrations.RenameField(
            model_name='coursedetail',
            old_name='courseAbout',
            new_name='module_course',
        ),
        migrations.RemoveField(
            model_name='coursedetail',
            name='banner_course',
        ),
        migrations.RemoveField(
            model_name='mentorachievment',
            name='image_worked',
        ),
        migrations.AddField(
            model_name='coursedetail',
            name='course_title',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='course_app.course'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Banner',
        ),
        migrations.AddField(
            model_name='mentor',
            name='workPlace',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course_app.mentorwork'),
        ),
        migrations.AlterField(
            model_name='coursedetail',
            name='mentorDescription',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course_app.mentor'),
        ),
        migrations.AlterField(
            model_name='mentorachievment',
            name='mentor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='achievements', to='course_app.mentor'),
        ),
        migrations.DeleteModel(
            name='Mentors',
        ),
    ]
