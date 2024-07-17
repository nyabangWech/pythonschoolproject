from django.db import models

class Classes(models.Model):
    number_of_seat= models.IntegerField()
    number_of_students=models.IntegerField()
    class_name = models.CharField(max_length=20)
    name_of_teachers=models.CharField(max_length=30)
    capacity=models.IntegerField(default=0)
    school_year=models.IntegerField()
    

def __str__(self):
        return f"{self.name_of_seat} {self.number_of_students}"
    
# Create your models here.
