from django.db import models
from teacher.models import Teacher
from course.models import  Course

class ClassPeriod(models.Model):
    Day_select=[
        ('Mon,Monday'),
        ('Tues,Tuesday'),
        ('WED,Wednesday'),
        ('THU,Thursday'),
        ('FRI, Friday'),
        ('SAT,satruday'),
        ('SUN,sunady'),
    ]
    teacher = models.ManyToManyField(Teacher)
    class_name = models.CharField(max_length=20)
    start_time = models.TimeField()
    end_time = models.TimeField()
    day_of_week = models.CharField(max_length=10) 
    courses= models.ManyToManyField(Course)
     
    objects=models.manager()
    

    def __str__(self):
        return f"{self.class_name} with {self.teacher} on {self.day_of_week} from {self.start_time} to {self.end_time}"



# Create your models here.
