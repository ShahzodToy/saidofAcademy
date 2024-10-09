from django.db import models
from django.utils.translation import gettext_lazy as _


class Partner(models.Model):
    image = models.ImageField(upload_to='partners')  # fixed typo 'parteners'

    class Meta:
        verbose_name = _('Partner')
        verbose_name_plural = _('Partners')  # added plural name

    def __str__(self):
        return f"Partner: {self.id}"  # more meaningful __str__


class StudentFeedback(models.Model):  # renamed to follow CamelCase
    message = models.TextField()
    full_name = models.CharField(max_length=125)
    profession = models.CharField(max_length=125)
    image = models.ImageField(upload_to='comment_student')  # consistent naming convention

    class Meta:
        verbose_name = _('Student Feedback')
        verbose_name_plural = _('Student Feedbacks')  # added plural name

    def __str__(self):
        return self.full_name


class FAQ(models.Model):
    question = models.CharField(max_length=125)
    answer = models.CharField(max_length=255)  # expanded to allow longer answers
    date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('FAQ')
        verbose_name_plural = _('FAQs')  # added plural name

    def __str__(self):
        return self.question


class DevelopingProgram(models.Model):
    logo = models.ImageField(upload_to='developing_program')  # consistent naming
    title = models.CharField(max_length=125)
    description = models.TextField()

    class Meta:
        verbose_name = _('Developing Program')
        verbose_name_plural = _('Developing Programs')  # added plural name

    def __str__(self):
        return self.title


class WhyUs(models.Model):
    image = models.ImageField(upload_to='why_us')  # consistent naming
    title = models.CharField(max_length=125)
    description = models.TextField()

    class Meta:
        verbose_name = _('Why Us')
        verbose_name_plural = _('Why Us')  # added plural name

    def __str__(self):
        return self.title


class DevelopingProgramDetail(models.Model):
    number = models.IntegerField()
    description = models.TextField()
    program_category = models.ForeignKey(DevelopingProgram, on_delete=models.CASCADE, related_name='details')  # fixed typo and added related_name for reverse lookup

    class Meta:
        verbose_name = _('Program Detail')
        verbose_name_plural = _('Program Details')  # added plural name

    def __str__(self):
        return f"{self.program_category.title} - Detail {self.number}"
