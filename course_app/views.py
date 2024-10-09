from django.shortcuts import render
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView
from .serializers import *
from .models import *

class CourseList(ListAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

class PlanCourse(ListAPIView):
    serializer_class = CoursePlanSerializer
    queryset = CoursePlan.objects.all()


class ContactView(CreateAPIView):
    serializer_class = ContactSerializer
    queryset =Contact.objects.all()


class ForWhomView(ListAPIView):
    serializer_class = ForWhomCourseSerializer
    queryset = ForWhomCourse.objects.all()


class ModuleView(ListAPIView):
    serializer_class =ModuleSerializer
    queryset = Module.objects.all()


class LessonView(ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class ComputerCharacterView(ListAPIView):
    serializer_class = ComputerCharacterSerializer
    queryset =ComputerCharacter.objects.all()


class MentorProfessionView(ListAPIView):
    serializer_class = MentorProfessionSerializer
    queryset = MentorProfession.objects.all()


class MentorView(ListAPIView):
    serializer_class = MentorSerializer
    queryset = Mentor.objects.all()


class MentorAchievmentView(ListAPIView):
    serializer_class = MentorAchievementSerializer
    queryset = MentorAchievement.objects.all()


class CourseDetailView(RetrieveAPIView):
    serializer_class = CourseDetailSerializer
    queryset = CourseDetail.objects.all()    






