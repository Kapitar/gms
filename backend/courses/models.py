from django.db import models
from users.models import Profile


class SchoolYear(models.Model):
    name = models.CharField(max_length=20)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name
    

class Quarter(models.Model):
    school_year = models.ForeignKey(SchoolYear, on_delete=models.CASCADE, related_name='quarters')
    name = models.CharField(max_length=20)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.name} ({self.school_year.name})"


class GradeSection(models.Model):
    name = models.CharField(max_length=255)
    weight = models.DecimalField(decimal_places=2, max_digits=4)
    
    def __str__(self):
        return f"{self.name} {self.weight}"


class Course(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey(Profile, limit_choices_to={'user_type': 'teacher'}, on_delete=models.CASCADE)
    school_year = models.ForeignKey(SchoolYear, on_delete=models.CASCADE, related_name='courses')

    def __str__(self):
        return f"{self.name} ({self.school_year.name})"


class Enrollment(models.Model):
    student = models.ForeignKey(Profile, limit_choices_to={'user_type': 'student'}, on_delete=models.CASCADE)
    enrolled_course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrollments')

    def __str__(self):
        return f"{self.student.user.username} in {self.enrolled_course.name}"


class Assignment(models.Model):
    name = models.CharField(max_length=100)
    max_points = models.PositiveIntegerField()
    due_date = models.DateField()
    assigned_course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='assignments')
    quarter = models.ForeignKey(Quarter, on_delete=models.CASCADE, related_name='assignments')
    grade_section = models.ForeignKey(GradeSection, on_delete=models.CASCADE, related_name='assignments', null=True)

    def __str__(self):
        return f"{self.name} ({self.assigned_course.name})"


class Grade(models.Model):
    student = models.ForeignKey(Profile, limit_choices_to={'user_type': 'student'}, on_delete=models.CASCADE)
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, related_name='grades')
    points_earned = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.student.user.username} - {self.assignment.name}: {self.points_earned}/{self.assignment.max_points}"