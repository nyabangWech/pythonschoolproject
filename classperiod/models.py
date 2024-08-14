from django.db import models


class Teacher(models.Model):
    name = models.CharField(max_length=100)
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
        return self.name

class Classes(models.Model):
    number_of_seat= models.IntegerField()
    number_of_students=models.IntegerField()
    class_name = models.CharField(max_length=20)
    name_of_teachers=models.CharField(max_length=30)
    capacity=models.IntegerField(default=0)
    school_year=models.IntegerField()
    

    def __str__(self):
        return self.name

class ClassPeriod(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    class_name = models.ForeignKey(Classes,on_delete=models.CASCADE)
    start_time = models.TimeField()
    end_time = models.TimeField()
    day_of_week = models.CharField(max_length=10)  

    def __str__(self):
        return f"{self.class_name} with {self.teacher} on {self.day_of_week} from {self.start_time} to {self.end_time}"



# Create your models here.
