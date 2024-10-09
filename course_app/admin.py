from django.contrib import admin
from .models import *


for a in [Course,Contact,ForWhomCourse,CoursePlan,ComputerCharacter,MentorProfession,MentorWork]:
    admin.site.register(a)


class ModuleInline(admin.TabularInline):
    model = Module
    extra = 2



class CourseDetailAdmin(admin.ModelAdmin):
    inlines = [ModuleInline]
    list_display = ('course_title','mentor')

admin.site.register(CourseDetail,CourseDetailAdmin)


class LessonInline(admin.TabularInline):
    model = Lesson
    extra = 1  # Number of empty lesson forms to display by default

# ModuleAdmin to display the inline lessons
class ModuleAdmin(admin.ModelAdmin):
    inlines = [LessonInline]  # Add the Lesson inline to the Module admin
    list_display = ('title',)  # Fields to display in the list view

# Register the models
admin.site.register(Module, ModuleAdmin)
admin.site.register(Lesson)



class MentorAchievmentInline(admin.TabularInline):
    model = MentorAchievement
    extra = 1  # Number of empty forms to display for adding new entries

class MentorWorkPlaceInline(admin.TabularInline):
    model = MentorWork
    extra = 2

@admin.register(Mentor)
class MentorsAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'position', 'experience')  # Display relevant fields in the list view
    inlines = [MentorAchievmentInline,MentorWorkPlaceInline]  # Attach the inline to the Mentors admin

@admin.register(MentorAchievement)
class MentorAchievmentAdmin(admin.ModelAdmin):
    list_display = ('title',)

