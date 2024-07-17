from django.db import models

class Classroom(models.Model):
    start_time= models.TimeField()
    end_time = models.TimeField()
    course = models.IntegerField()
    number_of_courses = models.IntegerField()
    name_of_teachers=models.CharField(max_length=30)
    new_classroom= models.CharField(max_length=255 ,null=True)
    course_prestiquies=models.TextField(blank=True,null=True)
    classroom = models.CharField(max_length=50)
    class_dayoftheweek= models.CharField(default='Monday', max_length=20)
    description_of_course=models.TextField(blank=True, null=True)
  
def __str__(self):
        return f"{self.name_of_course} {self.duration_of_course}"
    
# Create your models here.

# Create your models here.
