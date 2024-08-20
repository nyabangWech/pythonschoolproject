from django.db import models

class Classes(models.Model):
    Day_Choice=[
        ('Mon','Monday'),
        ('TUE','Tuesday'),
        ('WED','Wednesday'),
        ('THU','Thursday'),
        ('FRI','FRIDAY'),
        ('SAT','satruday'),
        ('SUN','sunday'),
    ]
    name= models.CharField(max_length=100,default='Default Name')
    number_of_seat= models.IntegerField()
    number_of_students=models.IntegerField()
    class_name = models.CharField(max_length=20)
    name_of_teachers=models.CharField(max_length=30)
    capacity=models.IntegerField(default=0)
    school_year=models.IntegerField()
    objects=models.Manager()
    

def __str__(self):
        return f"{self.name_of_seat} {self.number_of_students}"
    
# Create your models here.
