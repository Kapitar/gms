from rest_framework import serializers
from .models import SchoolYear, Quarter, GradeSection, Course, Enrollment, Assignment, Grade
from users.models import Profile
from users.serializers import UserSerializer, ProfileSerializer


class SchoolYearSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolYear
        fields = ['id', 'name', 'start_date', 'end_date']
        
        
class QuarterSerializer(serializers.ModelSerializer):
    school_year = SchoolYearSerializer()
    
    class Meta:
        model = Quarter
        fields = ['id', 'school_year', 'name', 'start_date', 'end_date']


class GradeSectionSerializer(serializers.ModelSerializer):    
    class Meta:
        model = GradeSection
        fields = ['id', 'name', 'weight']
        

class CourseSerializer(serializers.ModelSerializer):
    teacher = ProfileSerializer()
    school_year = SchoolYearSerializer()
    
    class Meta:
        model = Course
        fields = ['id', 'name', 'teacher', 'school_year']
        
        
class EnrollmentSerializer(serializers.ModelSerializer):
    student = ProfileSerializer()
    enrolled_course = CourseSerializer()
    
    class Meta:
        model = Enrollment
        fields = ['id', 'student', 'enrolled_course']
        

class AssignmentSerializer(serializers.ModelSerializer):
    assigned_course = CourseSerializer()
    quarter = QuarterSerializer()
    grade_section = GradeSectionSerializer()
    
    class Meta:
        model = Assignment
        fields = ['id', 'name', 'max_points', 'due_date', 'assigned_course', 'quarter', 'grade_section']
        

class GradeSerializer(serializers.ModelSerializer):
    assignment = AssignmentSerializer(read_only=True)
    assignment_id = serializers.PrimaryKeyRelatedField(
        queryset=Assignment.objects.all(), source='assignment', write_only=True)
    
    student = ProfileSerializer(read_only=True)
    student_id = serializers.PrimaryKeyRelatedField(
        queryset=Profile.objects.filter(user_type='student'), source='student', write_only=True)

    class Meta:
        model = Grade
        fields = ['id', 'student_id', 'student', 'assignment', 'assignment_id', 'points_earned']