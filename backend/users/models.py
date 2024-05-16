from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    USER_TYPE_CHOICES = [
        ('student', 'Student'),
        ('teacher', 'Teacher'),
        ('admin', 'Admin'),
        ('parent', 'Parent'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
    
    
class ParentChild(models.Model):
    parent = models.ForeignKey(Profile, limit_choices_to={'user_type': 'parent'}, on_delete=models.CASCADE, related_name='children')
    child = models.ForeignKey(Profile, limit_choices_to={'user_type': 'student'}, on_delete=models.CASCADE, related_name='parents')

    def __str__(self):
        return f"{self.parent.user.first_name} {self.parent.user.last_name} ({self.child.user.first_name} {self.child.user.last_name})"