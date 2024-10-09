from django.urls import path
from .views import *

urlpatterns = [
    path('partner',PartnerView.as_view()),
    path('feedback-student',FeedbackStudentView.as_view()),
    path('developing-program',DevelopingProgramView.as_view()),
    path('why-us',WhyUsView.as_view()),
    path('program-category/<int:pk>',DevelopingProgramDetail.as_view())
    
   
]