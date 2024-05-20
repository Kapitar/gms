from rest_framework import generics
from .models import Grade
from .serializers import GradeSerializer
from users.permissions import IsStudent, IsAdmin, IsParent
from rest_framework.exceptions import PermissionDenied, ValidationError, NotFound
from .permissions import IsGradeAccess


class ListGradeAPIView(generics.ListAPIView):
    serializer_class = GradeSerializer
    permission_classes = [IsStudent | IsParent | IsAdmin]
    
    def get_queryset(self):
        user = self.request.user
        student_id = self.kwargs['student_id']
      
        if user.profile.user_type == "student" and user.id != student_id:
            raise PermissionDenied("You do not have permissions to see the grades.")

        return Grade.objects.filter(student_id=student_id)
    
    
class CreateGradeAPIView(generics.CreateAPIView):
    serializer_class = GradeSerializer

    def perform_create(self, serializer):
        user = self.request.user
        student_id = serializer.validated_data['student'].id
        if user.profile.user_type != "admin" and user.profile.user_type != "teacher":
            raise PermissionDenied(detail="You are not a teacher to perform this action")
        
        if user.profile.user_type == "teacher" and serializer.validated_data['assignment'].assigned_course.teacher != user.profile:
            raise PermissionDenied(detail="You do not have permissions to grade this assignment.")
        
        if Grade.objects.filter(student_id=student_id, assignment=serializer.validated_data['assignment']).exists():
            raise ValidationError({'detail': 'Grade already exists.'})
        
        serializer.save()


class DestroyGradeAPIView(generics.DestroyAPIView):
    serializer_class = GradeSerializer
    queryset = Grade.objects.all()
    permission_classes = [IsGradeAccess]
    
    
class RetrieveGradeAPIView(generics.RetrieveAPIView):
    serializer_class = GradeSerializer
    queryset = Grade.objects.all()
    permission_classes = [IsGradeAccess]
    
    
    def get_object(self):
        student_id = self.kwargs['student_id']
        assignment_id = self.kwargs['assignment_id']
        user = self.request.user
        
        try:
            grade = Grade.objects.get(student_id=student_id, assignment_id=assignment_id)
        except Grade.DoesNotExist:
            raise NotFound("Grade not found.")
        
        # Permission checks
        if user.profile.user_type == "student" and user.profile.id != int(student_id):
            raise PermissionDenied("Students can only view their own grades.")
        if user.profile.user_type not in ["teacher", "admin"] and user.profile.id != int(student_id):
            raise PermissionDenied("You do not have permission to view this grade.")

        return grade