from rest_framework import serializers
from .models import *


class ForWhomCourseSerializer(serializers.ModelSerializer):
     # set to read-only for nested data

    class Meta:
        model = ForWhomCourse
        fields = ('id', 'title', 'description',)

class CourseSerializer(serializers.ModelSerializer):
    for_Whom = ForWhomCourseSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = ('id', 'title', 'description', 'logo','for_Whom')


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('full_name', 'phone_number', 'course', 'date')





class CoursePlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoursePlan
        fields = ('id', 'total_time', 'total_month', 'half_time', 'title', 'title_2', 'description', 'description_2')


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ('id', 'title')


class ModuleSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True, read_only=True)  # set lessons as nested read-only

    class Meta:
        model = Module
        fields = ('id', 'title', 'lessons')


class ComputerCharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComputerCharacter
        fields = ('id', 'processor', 'cpu', 'video_card', 'screen_size')


class MentorProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MentorProfession
        fields = ('id', 'title')


class MentorWorkPlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = MentorWork
        fields = ('id', 'image')


class MentorAchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = MentorAchievement
        fields = ('id', 'title')


class MentorSerializer(serializers.ModelSerializer):
    achievements = MentorAchievementSerializer(many=True, read_only=True)
    workplace = MentorWorkPlaceSerializer(many=True, read_only=True)

    class Meta:
        model = Mentor
        fields = ('id', 'full_name', 'profession', 'image', 'experience', 'position', 'achievements', 'workplace')


class CourseDetailSerializer(serializers.ModelSerializer):
    course_title = CourseSerializer(read_only=True)
    plan_course = CoursePlanSerializer(read_only=True)
    course_module = ModuleSerializer(read_only=True,many=True)
    mentor = MentorSerializer(read_only=True)

    class Meta:
        model = CourseDetail
        fields = ('id', 'course_title', 'plan_course', 'course_module', 'mentor')

