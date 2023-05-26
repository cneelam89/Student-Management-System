from django.db import models

# Create your models here.
class Student(models.Model):
    fname=models.CharField(max_length=25)
    lname=models.CharField(max_length=25)
    email=models.EmailField(max_length=25)
