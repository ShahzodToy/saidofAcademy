from django.db import models
from django.utils.translation import gettext_lazy as _


class Course(models.Model):
    title = models.CharField(max_length=125)
    description = models.TextField()
    logo = models.ImageField(upload_to='courses')

    class Meta:
        verbose_name = _('Course')
        verbose_name_plural = _('Courses')

    def __str__(self):
        return self.title


class Contact(models.Model):
    full_name = models.CharField(max_length=125)
    phone_number = models.CharField(max_length=125)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    is_checked = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _('Contact')
        verbose_name_plural = _('Contacts')

    def __str__(self):
        return f'{self.full_name} for {self.course.title}'


class ForWhomCourse(models.Model):
    title = models.CharField(max_length=125)
    description = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE,related_name='for_Whom')

    class Meta:
        verbose_name = _('ForWhomCourse')
        verbose_name_plural = _('ForWhomCourses')

    def __str__(self):
        return self.title


class CoursePlan(models.Model):
    total_time = models.CharField(max_length=125)
    total_month = models.CharField(max_length=125)
    half_time = models.CharField(max_length=125)
    title = models.CharField(max_length=125)
    title_2 = models.CharField(max_length=125)
    description_2 = models.TextField()
    description = models.TextField()

    class Meta:
        verbose_name = _('CoursePlan')
        verbose_name_plural = _('CoursePlans')

    def __str__(self):
        return self.title


class Lesson(models.Model):
    title = models.CharField(max_length=125)
    module_lesson = models.ForeignKey('Module', on_delete=models.CASCADE, related_name='lessons')

    class Meta:
        verbose_name = _('Lesson')
        verbose_name_plural = _('Lessons')

    def __str__(self):
        return self.title


class Module(models.Model):
    title = models.CharField(max_length=125)
    course_module = models.ForeignKey('CourseDetail',on_delete=models.CASCADE, related_name='course_module')

    class Meta:
        verbose_name = _('Module')
        verbose_name_plural = _('Modules')

    def __str__(self):
        return self.title


class ComputerCharacter(models.Model):
    processor = models.IntegerField()  # corrected field name
    cpu = models.CharField(max_length=125)
    video_card = models.CharField(max_length=125)
    screen_size = models.CharField(max_length=125)

    class Meta:
        verbose_name = _('ComputerCharacter')
        verbose_name_plural = _('ComputerCharacters')

    def __str__(self):
        return f'Computer {self.video_card}'


class MentorProfession(models.Model):
    title = models.CharField(max_length=125)

    class Meta:
        verbose_name = _('MentorProfession')
        verbose_name_plural = _('MentorProfessions')

    def __str__(self):
        return self.title


class Mentor(models.Model):
    full_name = models.CharField(max_length=125)
    image = models.ImageField(upload_to='mentors')
    experience = models.CharField(max_length=125)
    position = models.CharField(max_length=125)
    profession = models.ForeignKey(MentorProfession, on_delete=models.CASCADE, related_name='mentors')

    class Meta:
        verbose_name = _('Mentor')
        verbose_name_plural = _('Mentors')

    def __str__(self):
        return self.full_name


class MentorAchievement(models.Model):
    title = models.CharField(max_length=125)
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE, related_name='achievements')

    class Meta:
        verbose_name = _('MentorAchievement')
        verbose_name_plural = _('MentorAchievements')

    def __str__(self):
        return self.title


class MentorWork(models.Model):
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE, related_name='workplace')
    image = models.ImageField(upload_to='worked_place')

    class Meta:
        verbose_name = _('MentorWorkPlace')
        verbose_name_plural = _('MentorWorkPlaces')


class CourseDetail(models.Model):
    course_title = models.ForeignKey(Course, on_delete=models.CASCADE)
    plan_course = models.ForeignKey(CoursePlan, on_delete=models.CASCADE)
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    computer_character = models.ForeignKey(ComputerCharacter, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('CourseDetail')
        verbose_name_plural = _('CourseDetails')

    def __str__(self):
        return self.course_title.title