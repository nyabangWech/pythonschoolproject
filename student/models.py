from django.db import models

class Student(models.Model):
    first_name= models.CharField(max_length=20)
    last_name= models.CharField(max_length=20)
    email= models.EmailField()
    date_of_birth= models.DateField()
    code =models.PositiveSmallIntegerField()
    country = models.CharField(max_length= 20)
    gender =models.CharField(max_length=6)
    id_number = models.IntegerField()
    enrollment_date=models.DateField()
    guardian_phonenumber=models.CharField(max_length=20)
    student_guardian=models.CharField(max_length=12)
    # class_id=models.ForeignKey()
    # student_picture=models.ImageField()
    bio = models.TextField()
    
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# Create your models here.
