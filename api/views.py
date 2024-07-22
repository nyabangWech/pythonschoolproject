from django.shortcuts import render
from rest_framework.response import Response
from  rest_framework.views import APIView
from  student.models import Student
from classroom.models import Classroom
from classes.models import Classes
from teacher.models import Teacher
from course.models import Course
from .serializers import  StudentSerializer
from.serializers import ClassroomSerializer
from.serializers import ClassesSerializer
from .serializers import  TeacherSerializer
from .serializers import CourseSerializer
from  rest_framework.views import status




class StudentListView(APIView):
    def get(self,request):
        student=Student.objects.all
        serializer=StudentSerializer(student,many=True)
        return Response(serializer.data)
    def post(self,request):
        Serializer=StudentSerializer(data= request.data)
        if Serializer.is_valid():
            Serializer.save()
            return Response(Serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(Serializer.errors,status= status.HTTP_400_BAD_REQUEST)
class ClassroomListView(APIView):
    def get(self,request):
        classroom=Classroom.objectseacherserializers.all
        serializer=ClassroomSerializer(classroom,many=True)
        return Response(serializer.data)
    def post(self,request):
        Serializer=StudentSerializer(data= request.data)
        if Serializer.is_valid():
            Serializer.save()
            return Response(Serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(Serializer.errors,status= status.HTTP_400_BAD_REQUEST)
        
        
class ClassesListView(APIView):
    def get(self,request):
        classes = Classes.objects.all
        serializer=ClassesSerializer(classes,many=True)
        return Response(serializer.data)
    def post(self,request):
        Serializer=ClassesSerializer(data= request.data)
        if Serializer.is_valid():
            Serializer.save()
            return Response(Serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(Serializer.errors,status= status.HTTP_400_BAD_REQUEST)
        
class TeacherListView(APIView):
    def get(self,request):
        teacher=Teacher.objects.all
        serializer= TeacherSerializer(teacher,many=True)
        return Response(serializer.data)
    def post(self,request):
        Serializer=TeacherSerializer(data= request.data)
        if Serializer.is_valid():
            Serializer.save()
            return Response(Serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(Serializer.errors,status= status.HTTP_400_BAD_REQUEST)
        
class CourseListView(APIView):
    def get(self,request):
        course=Course.objects.all
        serializer=CourseSerializer(course,many=True)
        return Response(serializer.data)
    def post(self,request):
        Serializer=CourseSerializer(data= request.data)
        if Serializer.is_valid():
            Serializer.save()
            return Response(Serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(Serializer.errors,status= status.HTTP_400_BAD_REQUEST)
        
    
class StudentDetailView(APIView):
    def get(self,request,id):
        Student=Student.objects.all.get(id=id)
        serializer =StudentSerializer(Student)
        return Response(serializer.data)
    def put(self,request,id):
        Student= Student.objects.get(id=id)
        serializer=StudentSerializer(Student,data=request.data)
        if serializer.is_valid():
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,id):
      Student= Student.objects.get(id=id)
      Student.delete()
      return Response(status=status.HTTP_202_ACCEPTED)
  
  
class classroomDetailView(APIView):
    def get(self,request,id):
        Classroom=Classroom.objects.all.get(id=id)
        serializer =ClassroomSerializer(Classroom)
        return Response(serializer.data)
    
    def put(self,request,id):
        Classroom= Classroom.objects.get(id=id)
        serializer=ClassroomSerializer(Classroom,data=request.data)
        if serializer.is_valid():
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,id):
      Classroom= Classroom.objects.get(id=id)
      Classroom.delete()
      return Response(status=status.HTTP_202_ACCEPTED)



class classesDetailView(APIView):
    def get(self,request,id):
        Classes=Classes.objects.all.get(id=id)
        serializer =ClassesSerializer(Classroom)
        return Response(serializer.data)
    
    def put(self,request,id):
        Classes= Classes.objects.get(id=id)
        serializer=ClassesSerializer(Classes,data=request.data)
        if serializer.is_valid():
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,id):
      Classes= Classes.objects.get(id=id)
      Classes.delete()
      return Response(status=status.HTTP_202_ACCEPTED)
  
  
class courseDetailView(APIView):
    def get(self,request,id):
        Course=Course.objects.all.get(id=id)
        serializer =CourseSerializer(Course)
        return Response(serializer.data)
    
    def put(self,request,id):
        Course= Course.objects.get(id=id)
        serializer=CourseSerializer(Course,data=request.data)
        if serializer.is_valid():
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,id):
      Course= Course.objects.get(id=id)
      Course.delete()
      return Response(status=status.HTTP_202_ACCEPTED)
  

class teacherDetailView(APIView):
    def get(self,request,id):
        Teacher=Teacher.objects.all.get(id=id)
        serializer =CourseSerializer(Course)
        return Response(serializer.data)
    
    def put(self,request,id):
        Teacher= Teacher.objects.get(id=id)
        serializer=TeacherSerializer(Course,data=request.data)
        if serializer.is_valid():
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,id):
      Teacher= Teacher.objects.get(id=id)
      Teacher.delete()
      return Response(status=status.HTTP_202_ACCEPTED)
  
  
  
  
  

  
        




  
  
  

  
        



