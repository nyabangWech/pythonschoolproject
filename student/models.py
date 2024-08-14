from django.db import models
from course.models import Course
from classes.models import Classes


class Student(models.Model):
    first_name= models.CharField(max_length=20)
    last_name= models.CharField(max_length=20)
    email= models.EmailField()
    date_of_birth= models.DateField()
    code =models.PositiveSmallIntegerField()
    country = models.CharField(max_length= 20)
    gender =models.CharField(max_length=6)
    courses=models.ManyToManyField(Course, related_name='student')
    classes=models.ManyToManyField(Classes,related_name='student')
    id_number = models.IntegerField()
    bio = models.TextField()
   
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# Create your models here.
