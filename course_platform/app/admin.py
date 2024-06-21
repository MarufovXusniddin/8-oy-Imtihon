from django.contrib import admin
from .models import Course, Student, Teacher, Group, Lesson, Comment, LikeDislike, Update

# Register your models here.


class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price')
    list_display_links = ('title',)


class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'phone_number', 'email')
    list_display_links = ('full_name',)


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'phone', 'experience')
    list_display_links = ('full_name',)


class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'course', 'number')
    list_display_links = ('course',)


class LessonAdmin(admin.ModelAdmin):
    list_display = ('id', 'topic', 'number', 'comment', 'group')
    list_display_links = ('topic',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'lesson', 'text', 'author', 'pub_date')
    list_display_links = ('lesson',)


class LikeDislikeAdmin(admin.ModelAdmin):
    list_display = ('id', 'lesson', 'user', 'value')
    list_display_links = ('lesson',)


class UpdateAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'created_at')
    list_display_links = ('title',)


admin.site.register(Course, CourseAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(LikeDislike, LikeDislikeAdmin)
admin.site.register(Update, UpdateAdmin)
