from django.test import TestCase
from .models import (
    Course, Contact, forWhomCourse, CoursePlan,
    Lesson, Module, ComputerCharacter,
    MentorProfession, Mentor, MentorAchievment,
    CourseDetail
)

class CourseModelTest(TestCase):
    def test_create_course(self):
        course = Course.objects.create(title='Python Course', description='Learn Python.', logo='path/to/logo.jpg')
        self.assertEqual(course.title, 'Python Course')
        self.assertIn('Learn Python', course.description)

class OrderCourseModelTest(TestCase):
    def test_create_order_course(self):
        course = Course.objects.create(title='Java Course', description='Learn Java.', logo='path/to/logo.jpg')
        order = Contact.objects.create(full_name='Jane Doe', phone_number='1234567890', course=course)
        self.assertEqual(order.full_name, 'Jane Doe')
        self.assertEqual(order.course.title, 'Java Course')


class PlanCourseModelTest(TestCase):
    def test_create_plan_course(self):
        plan = CoursePlan.objects.create(
            total_time='3 months',
            total_month='3',
            half_time='1.5 months',
            title='Full Course Plan',
            title_2='Intermediate Plan',
            description_2='For intermediate learners.',
            description='Comprehensive course plan.'
        )
        self.assertEqual(plan.title, 'Full Course Plan')
        self.assertIn('intermediate learners', plan.description_2)

class LessonModelTest(TestCase):
    def test_create_lesson(self):
        module = Module.objects.create(title='Python Basics')
        lesson = Lesson.objects.create(title='Introduction to Python', module_lesson=module)
        self.assertEqual(lesson.title, 'Introduction to Python')
        self.assertEqual(lesson.module_lesson.title, 'Python Basics')

class ModuleModelTest(TestCase):
    def test_create_module(self):
        module = Module.objects.create(title='Django Basics')
        self.assertEqual(module.title, 'Django Basics')


class ComputerCharacterModelTest(TestCase):
    def test_create_computer_character(self):
        character = ComputerCharacter.objects.create(protsetsor=4, cpu='Intel i7', video_cart='NVIDIA GTX 1650', screen_size='15.6 inches')
        self.assertEqual(character.cpu, 'Intel i7')

class MentorProfessionModelTest(TestCase):
    def test_create_mentor_profession(self):
        profession = MentorProfession.objects.create(title='Data Scientist')
        self.assertEqual(profession.title, 'Data Scientist')

class MentorsModelTest(TestCase):
    def test_create_mentor(self):
        profession = MentorProfession.objects.create(title='Web Developer')
        mentor = Mentor.objects.create(full_name='John Smith', image='path/to/image.jpg', level='Senior', experience='5 years', position='Lead Developer', profession=profession)
        self.assertEqual(mentor.full_name, 'John Smith')

class MentorAchievmentModelTest(TestCase):
    def test_create_mentor_achievement(self):
        mentor = Mentor.objects.create(full_name='Alice Johnson', image='path/to/image.jpg', level='Expert', experience='10 years', position='Senior Developer', profession=MentorProfession.objects.create(title='Software Engineer'))
        achievement = MentorAchievment.objects.create(title='Best Teacher Award', image_worked='path/to/award.jpg', mentor=mentor)
        self.assertEqual(achievement.title, 'Best Teacher Award')

