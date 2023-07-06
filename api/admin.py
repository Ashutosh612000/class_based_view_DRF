from django.contrib import admin
from api.models import Course

class CourseAdmin(admin.ModelAdmin):
    list_display = ['name','author','price']

admin.site.register(Course, CourseAdmin)