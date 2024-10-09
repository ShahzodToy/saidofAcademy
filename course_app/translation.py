from .models import *
from modeltranslation.translator import TranslationOptions, translator

class CourseTranslation(TranslationOptions):
    fields = ('title', 'description')


class forWhomCourseTranslation(TranslationOptions):
    fields = ('title', 'description')


class PlanCourseTranslation(TranslationOptions):
    fields = ('total_month','half_time','title','description','title_2','description_2')


class LessonTranslator(TranslationOptions):
    fields = ('title',)


class MentorTranslator(TranslationOptions):
    fields = ('position',)


class ModuleTranslator(TranslationOptions):
    fields=('title',)


class MentorProfessionTranslation(TranslationOptions):
    fields = ('title',)


class MentorAchievmentTranslation(TranslationOptions):
    fields = ('title',)



for a,b in [(Course,CourseTranslation),(ForWhomCourse,forWhomCourseTranslation),(CoursePlan,PlanCourseTranslation),(Lesson,LessonTranslator),(Module,ModuleTranslator),(MentorAchievement,MentorAchievmentTranslation),(MentorProfession,MentorProfessionTranslation),(Mentor,MentorTranslator)]:
    translator.register(a,b)