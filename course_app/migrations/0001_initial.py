# Generated by Django 4.2 on 2024-10-03 07:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=125)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='banner')),
            ],
        ),
        migrations.CreateModel(
            name='ComputerCharacter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('protsetsor', models.IntegerField()),
                ('cpu', models.CharField(max_length=125)),
                ('video_cart', models.CharField(max_length=125)),
                ('screen_size', models.CharField(max_length=125)),
            ],
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=125)),
                ('title', models.CharField(max_length=125)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=125)),
                ('description', models.TextField()),
                ('logo', models.ImageField(upload_to='courses')),
            ],
        ),
        migrations.CreateModel(
            name='forWhomCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=125)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='MentorAchievment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=125)),
                ('image_worked', models.ImageField(upload_to='achivements')),
            ],
        ),
        migrations.CreateModel(
            name='MentorProfession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=125)),
            ],
        ),
        migrations.CreateModel(
            name='PlanCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_time', models.CharField(max_length=125)),
                ('total_month', models.CharField(max_length=125)),
                ('half_time', models.CharField(max_length=125)),
                ('title', models.CharField(max_length=125)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='OrderCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=125)),
                ('phone_number', models.CharField(max_length=125)),
                ('date', models.DateTimeField(auto_now=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course_app.course')),
            ],
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('title', models.CharField(max_length=125)),
                ('content_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course_app.content')),
            ],
        ),
        migrations.CreateModel(
            name='Mentors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=125)),
                ('image', models.ImageField(upload_to='mentors')),
                ('level', models.CharField(max_length=125)),
                ('experience', models.CharField(max_length=125)),
                ('achivement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course_app.mentorachievment')),
                ('profession', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course_app.mentorprofession')),
            ],
        ),
        migrations.CreateModel(
            name='CourseDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banner_course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course_app.banner')),
                ('computer_char', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course_app.computercharacter')),
                ('courseAbout', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course_app.module')),
                ('forWhom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course_app.forwhomcourse')),
                ('mentorDescription', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course_app.mentors')),
                ('planCourse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course_app.plancourse')),
            ],
        ),
    ]