from django.urls import path
from .views import *


urlpatterns = [
    path('courses-list',CourseList.as_view()),
    # path('course-plan',PlanCourse.as_view()),
    path('contact',ContactView.as_view()),
    # path('forwhom',ForWhomView.as_view()),
    # path('modules',ModuleView.as_view()),
    path('computer-character',ComputerCharacterView.as_view()),
    path('mentors',MentorView.as_view()),
    # path('mentor-achievment',MentorAchievmentView.as_view()),
    # path('content',LessonView.as_view()),
    path('course-detail/<int:pk>',CourseDetailView.as_view()),

]