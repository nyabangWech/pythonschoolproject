from django.db import models

class Teacher(models.Model):
    first_name= models.CharField(max_length=20)
    last_name= models.CharField(max_length=20)
    email= models.EmailField()
    date_of_birth= models.DateField()
    Nationality = models.CharField(max_length= 20)
    status=models.BooleanField(default=False)
    gender =models.CharField(max_length=6)
    level_of_education=models.CharField(max_length=20)
    salary=models.IntegerField()
    id_number = models.IntegerField()
    teacher = models.ForeignKey('Teacher', on_delete=models.SET_NULL, null=True, blank=True, related_name='courses')
    bio = models.TextField()
    
    
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
# Create your models here.
