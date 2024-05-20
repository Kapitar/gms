from rest_framework import permissions


class IsGradeAccess(permissions.BasePermission):    
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return request.user.profile.user_type == "admin" or request.user.profile.user_type == "teacher"

    def has_object_permission(self, request, view, obj): 
        if request.method in permissions.SAFE_METHODS:
            return obj.student == request.user.profile
               
        return request.user.profile.user_type == "admin" or (
            request.user.profile.user_type == "teacher" and
            obj.assignment.assigned_course.teacher == request.user.profile
        )