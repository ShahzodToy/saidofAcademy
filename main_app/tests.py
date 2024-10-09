from django.test import TestCase
from django.test import TestCase
from .models import Partner, studentFeedback, FAQ, DevelopingProgram, WhyUs, DevelopingProgramDetail

class PartnerModelTest(TestCase):
    def test_create_partner(self):
        partner = Partner.objects.create(image='image.jpg')
        self.assertEqual(partner.image.name, 'image.jpg')  # Adjust as per your image path

class CommentStudentModelTest(TestCase):
    def test_create_comment_student(self):
        comment = studentFeedback.objects.create(
            message='This is a test message.',
            full_name='John Doe',
            profession='Student',
            image='path/to/comment_image.jpg'
        )
        self.assertEqual(comment.full_name, 'John Doe')
        self.assertEqual(comment.message, 'This is a test message.')

class FAQModelTest(TestCase):
    def test_create_faq(self):
        faq = FAQ.objects.create(
            question='What is Django?',
            answer='Django is a web framework.',
        )
        self.assertEqual(faq.question, 'What is Django?')
        self.assertEqual(faq.answer, 'Django is a web framework.')

class DevelopingProgramModelTest(TestCase):
    def test_create_developing_program(self):
        program = DevelopingProgram.objects.create(
            logo='path/to/logo.jpg',
            title='Django Course',
            description='Learn Django from scratch.'
        )
        self.assertEqual(program.title, 'Django Course')
        self.assertIn('Learn Django', program.description)

class WhyUsModelTest(TestCase):
    def test_create_why_us(self):
        why_us = WhyUs.objects.create(
            image='path/to/why_us_image.jpg',
            title='Why Choose Us',
            description='We offer the best programs.'
        )
        self.assertEqual(why_us.title, 'Why Choose Us')
        self.assertIn('best programs', why_us.description)

class AboutProgramModelTest(TestCase):
    def test_create_about_program(self):
        program = DevelopingProgram.objects.create(
            logo='path/to/logo.jpg',
            title='Django Course',
            description='Learn Django from scratch.'
        )
        about_program = DevelopingProgramDetail.objects.create(
            id=1,
            description='This program covers Django basics.',
            program_categoty=program
        )
        self.assertEqual(about_program.number, 1)
        self.assertIn('covers Django', about_program.description)
        self.assertEqual(about_program.program_categoty.title, 'Django Course')