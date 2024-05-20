from rest_framework import permissions


class IsStudent(permissions.BasePermission):
    def has_permission(self, request, view):
        user_type = request.user.profile.user_type
        return user_type == 'student'
    

class IsParent(permissions.BasePermission):
    def has_permission(self, request, view):
        user_type = request.user.profile.user_type
        return user_type == 'parent'


class IsTeacher(permissions.BasePermission):
    def has_permission(self, request, view):
        user_type = request.user.profile.user_type
        return user_type == "teacher"


class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.profile.user_type == 'admin'