from modeltranslation.translator import TranslationOptions, translator
from .models import *


class CommentStudentTranslator(TranslationOptions):
    fields= ('message',)


class FAQTranslator(TranslationOptions):
    fields = ('question','answer',)


class DevelopingProgramTranslator(TranslationOptions):
    fields = ('title','description')

class WhyUsTranslator(TranslationOptions):
    fields = ('title','description')

class AboutProgramTranslator(TranslationOptions):
    fields = ('description',)



for a,b in [(StudentFeedback,CommentStudentTranslator),(FAQ,FAQTranslator),(DevelopingProgram,DevelopingProgramTranslator),(WhyUs,WhyUsTranslator),(DevelopingProgramDetail,AboutProgramTranslator)]:

    translator.register(a,b)
