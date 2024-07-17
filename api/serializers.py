from  rest_framework import serializers
from student.models import Student
from classroom.models import Classroom
from classes.models import Classes
from course.models import Course
from teacher.models import Teacher

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
          