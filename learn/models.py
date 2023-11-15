from django.db import models
from main.models import User

# this model is for teachers
class TeacherCustomizer(models.Model):
    teacher = models.OneToOneField(User, on_delete=models.CASCADE)
    school = models.TextField(max_length=30, blank=False)
    subject_taught = models.TextField(max_length=30, blank=False)

class LearnerCustomizer(models.Model):
    student = models.OneToOneField(User, on_delete=models.CASCADE)
    school = models.TextField(max_length=30, blank=False)
    birth_date = models.DateTimeField(blank=False)
    future_career = models.TextField(max_length=20, blank=True)
    teacher = models.ManyToManyField(TeacherCustomizer, on_delete=models.SET_NULL)



