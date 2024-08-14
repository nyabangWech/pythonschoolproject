from django.db import models

class Course(models.Model):
    name_of_course= models.CharField(max_length=20)
    startyear_of_course= models.DateField()
    number_of_students= models.IntegerField()
    ID_of_course = models.IntegerField()
    name_of_teacher=models.CharField(max_length=30)
    course_prestiquies=models.TextField(blank=True,null=True)
    description_of_course=models.TextField(blank=True, null=True)

def __str__(self):
        return f"{self.name_of_course} {self.duration_of_course}"
    
# Create your models here.
