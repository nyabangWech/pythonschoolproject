from  rest_framework import serializers
from student.models import Student
from classroom.models import Classroom
from classes.models import Classes
from course.models import Course
from teacher.models import Teacher
from classperiod.models import ClassPeriod

class StudentSerializer(serializers.ModelSerializer):
      class Meta:
           model= Student
           fields="__all__"
class ClassroomSerializer(serializers.ModelSerializer):
      class Meta:
           model= Classroom
           fields="__all__"

class ClassesSerializer(serializers.ModelSerializer):
      class Meta:
           model= Classes
           fields="__all__"
class CourseSerializer(serializers.ModelSerializer):
      class Meta:
           model= Course
           fields="__all__"
class TeacherSerializer(serializers.ModelSerializer):
      class Meta:
           model= Teacher
           fields="__all__"
class AddStudent(serializers.Serializer):
      student_id = serializers.IntegerField()
      class_id= serializers.IntegerField()
      
class classperiodSerializer(serializers.ModelSerializer):
      teacher =TeacherSerializer()
      Classes= ClassesSerializer()
      class Meta:
       Model=ClassPeriod
       field="_all_"
class minimalClass_PeriodSerializer(serializers.ModelSerializer):
    period_name = serializers.SerializerMethodField()
    def get_period_name(self,object):
        return f"{object.name}"
    class Meta:
        model = ClassPeriod
        fields = ["name","class_period_classroom","period_name"]  
class minimalClassesSerializer(serializers.ModelSerializer):
    check_name = serializers.SerializerMethodField()

    def get_check_name(self, object): 
        return f"{object.name}"  
class minimalStudentSerializers(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    def get_full_name(self,object):
        return f"{object.first_name} {object.last_name}"
    class Meta:
        model=Student
        fields=["full_name","email"]   
