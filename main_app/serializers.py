from .models import *
from rest_framework import serializers


class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = ('id', 'image')


class CommentStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentFeedback  # updated to match CamelCase model name
        fields = ('id', 'message', 'full_name', 'profession', 'image')


class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = ('id', 'question', 'answer', 'date')  # removed 'is_checked' and 'faq_category' since they are not in the model


class DevelopingProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = DevelopingProgram
        fields = ('id', 'logo', 'title', 'description')


class WhyUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhyUs
        fields = ('id', 'title', 'description')


class DevelopingProgramDetailSerializer(serializers.ModelSerializer):  # fixed typo in class name

    class Meta:
        model = DevelopingProgramDetail
        fields = ('id', 'number', 'description', 'program_category')  # corrected 'program_categoty' to 'program_category'
