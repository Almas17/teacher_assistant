from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Users(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    is_student = models.BooleanField('student status', default=False)
    is_teacher = models.BooleanField('teacher status', default=False)
    created_at = models.DateTimeField(auto_now_add=True)
