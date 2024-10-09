from django.shortcuts import render
from rest_framework.generics import ListAPIView,RetrieveAPIView
from .models import *
from .serializers import *
from rest_framework.validators import ValidationError
from rest_framework.response import Response

class PartnerView(ListAPIView):
    serializer_class = PartnerSerializer
    queryset = Partner.objects.all()


class FeedbackStudentView(ListAPIView):
    serializer_class = CommentStudentSerializer
    queryset = StudentFeedback.objects.all()


class FAQView(ListAPIView):
    serializer_class = FAQSerializer
    queryset = FAQ.objects.all()

    
class DevelopingProgramView(ListAPIView):
    serializer_class = DevelopingProgramSerializer
    queryset = DevelopingProgram.objects.all()


class WhyUsView(ListAPIView):
    serializer_class = WhyUsSerializer
    queryset = WhyUs.objects.all()


class DevelopingProgramDetail(RetrieveAPIView):
    serializer_class = DevelopingProgramDetailSerializer
    queryset = DevelopingProgramDetail.objects.all()

