from django.contrib import admin
from .models import SchoolYear, Quarter, Course, Enrollment, Assignment, Grade, GradeSection

admin.site.register(SchoolYear)
admin.site.register(Quarter)
admin.site.register(Course)
admin.site.register(Enrollment)
admin.site.register(Assignment)
admin.site.register(Grade)
admin.site.register(GradeSection)