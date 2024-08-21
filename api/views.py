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
from.serializers import AddStudent
from.serializers import classperiodSerializer
from.serializers import minimalClassesSerializer
from.serializers import minimalStudentSerializers
from.serializers import minimalClass_PeriodSerializer


class StudentListView(APIView):
    def get(self,request):
        student=Student.objects.all()
        serializer=minimalStudentSerializers(student,many=True)
        first_name=request.query_params.get("first_name")
        country= request.query_params.get("country")
        if country:
         student=student.filter(country=country)
        if first_name:
         student=student.filter(first_name=first_name)
        serializer=StudentSerializer(student,many=True)
        return Response(serializer.data)
    def post(self,request):
        Serializer=StudentSerializer(data= request.data)
        if Serializer.is_valid():
            Serializer.save()
            return Response(Serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(Serializer.errors,status= status.HTTP_400_BAD_REQUEST)
class StudentDetailView(APIView):
    def get(self,request,id):
        Student=Student.objects.get(id=id)
        serializer =StudentSerializer(Student)
        return Response(serializer.data)
    def put(self,request,id):
        Student= Student.objects.get(id=id)
        serializer=StudentSerializer(Student,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,id):
      Student= Student.objects.get(id=id)
      Student.delete()
      return Response(status=status.HTTP_202_ACCEPTED)
    def enroll_student(self,student,course_id):
        course = Course.objects.get(id=course_id)
        student.courses.add(course)

    def unenroll_student(self,student,course_id):
        course = Course.objects.get(id=course_id)
        student.courses.remove(course)    

    
    def add_to_class(self, student, class_id):
        class_obj = Classes.objects.get(id=class_id)
        student.classes.add(class_obj)    

    def post(self,request,id):
        student = Student.objects.get(id=id)
        action = request.data.get("action") 

        if action == "enroll":
           course_id = request.data.get("course")
           self.enroll_student(student,course_id)
           return Response(status.HTTP_202_ACCEPTED)
        
        if action == "unenroll":
           course_id = request.data.get("course")
           self.unenroll_student(student,course_id)
           return Response(status.HTTP_202_ACCEPTED)
        
        elif action == "add_to_class":
            class_id = request.data.get("classes")
            self.add_to_class(student, class_id)
            return Response(status=status.HTTP_202_ACCEPTED)
        
        
        
class ClassroomListView(APIView):
    def get(self,request):
        classroom=Classroom.objects.all()
        serializer=ClassroomSerializer(classroom,many=True)
        return Response(serializer.data)
    def post(self,request):
        Serializer= ClassroomSerializer(data= request.data)
        if Serializer.is_valid():
            Serializer.save()
            return Response(Serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(Serializer.errors,status= status.HTTP_400_BAD_REQUEST)
        
        
class ClassesListView(APIView):
    def get(self,request):
        classes = Classes.objects.all()
        serializer=minimalClassesSerializer(classes,many=True)
        name=request.query_params.get("name")
        seat_arrangement=request.quert_params.get("sitting arrangement")
        if name:
            classes=classes.filter(name=name)
        if seat_arrangement:
            classes=classes.filter(seat_arrangement=seat_arrangement)
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
        teacher=Teacher.objects.all()
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
        course=Course.objects.all()
        serializer=CourseSerializer(course,many=True)
        return Response(serializer.data)
    def post(self,request):
        Serializer=CourseSerializer(data= request.data)
        if Serializer.is_valid():
            Serializer.save()
            return Response(Serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(Serializer.errors,status= status.HTTP_400_BAD_REQUEST)
class classesDetailView(APIView):
    def get(self,request,id):
        Classes=Classes.objects.get(id=id)
        serializer =ClassesSerializer(Classes)
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
      serializer =ClassesSerializer(Classes)
      Classes.delete()
      return Response(status=status.HTTP_202_ACCEPTED)
  
  
class courseDetailView(APIView):
    def get(self,request,id):
        Course=Student.objects.get(id=id)
        serializer =CourseSerializer(Course)
        return Response(serializer.data)
    
    def put(self,request,id):
        Course= Course.objects.get(id=id)
        serializer=CourseSerializer(Course,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,id):
      Course= Course.objects.get(id=id)
      serializer=CourseSerializer(Course)
      Course.delete()
      return Response( serializer.error,status=status.HTTP_400_BAD_REQUEST)
  

class teacherDetailView(APIView):
    def get(self,request,id):
        teacher =Teacher.objects.all.get(id=id)
        serializer =TeacherSerializer(teacher)
        return Response(serializer.data)
    
    def put(self,request,id):
        teacher= Teacher.objects.get(id=id)
        serializer=TeacherSerializer(Course,data=request.data)
        if serializer.is_valid():
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,id):
      teacher= Teacher.objects.get(id=id)
      Teacher.delete()
      return Response(status=status.HTTP_202_ACCEPTED)
  
    def assign_course(self, teacher, course_id):
        course = Course.objects.get(id=course_id)
        teacher.courses.add(course)

    def post(self, request, id):
        teacher = Teacher.objects.get(id=id)
        action = request.data.get("action")
        if action == "assign_course":
           course_id = request.data.get("course")
           self.assign_course(teacher,course_id)
           return Response(status.HTTP_202_ACCEPTED)

        return Response({"error": "Invalid action"}, status=status.HTTP_400_BAD_REQUEST)
        

  
  
  
class ClasssPeriodListView(APIView):
    def get(self, request):
        action = request.query_params.get('action')

        if action == 'weekly_timetable':
            return self.get_weekly_timetable(request)
        periods = class_period_classroom.objects.all()
        serializer = classperiodSerializer(periods, many=True)
        serializer = minimalClass_PeriodSerializer(periods,many=True)
        name= request.query_params.get("name")
        class_period_classroom = request.query_params.get("class period classroom")
        if name:
            periods = periods.filter(name == name)
        if class_period_classroom:
            periods = periods.filter(class_period_classroom == class_period_classroom)
        return Response(serializer.data)

    def get_weekly_timetable(self, request):
        start_date_str = request.query_params.get('start_date')
        if not start_date_str:
            start_date = datetime.now().date()
        else:
            try:
                start_date = parser.parse(start_date_str).date()
            except ValueError:
                return Response({"error": "Invalid date format. Please use YYYY-MM-DD."},
                                status=status.HTTP_400_BAD_REQUEST)

        end_date = start_date + timedelta(days=6)

        class_periods = class_periods.objects.filter(
            date__range=[start_date, end_date]
        ).select_related('teacher', 'course', 'class_obj')

        timetable = {}
        for period in class_periods:
            day = period.date.strftime('%A')
            if day not in timetable:
                timetable[day] = []
            
            timetable[day].append({
                'time': period.time.strftime('%H:%M'),
                'course': period.course.name,
                'teacher': f"{period.teacher.first_name} {period.teacher.last_name}",
                'class': period.class_obj.name
            })

        return Response(timetable)

    def post(self, request):
        serializer = ClassPeriodSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
class ClassPeriodDetailView(APIView):
    def get(self,request,id):
        period=ClassPeriod.objects.get(id=id)
        serializer =ClassPeriodSerializer(period)
        return Response(serializer.data)   

    def put(self, request,id):
       period=ClassPeriod.objects.get(class_id=id)
       serializer =ClassPeriodSerializer(period,data=request.data)
       if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
       else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)  

    def delete(self,request,id):
        period=Class_Period.objects.get(id=id)
        serializer =Class_PeriodSerializer(period)
        period.delete()
        return Response(serializer.errors,status=status.HTTP_202_ACCEPTED)  
    
    def post(self, request):
        serializer = Class_PeriodSerializer(data=request.data)
        if serializer.is_valid():
            class_period = serializer.save()
            
            teacher_id = request.data.get("teacher_id")
            course_id = request.data.get("course_id")
            
            if teacher_id and course_id:
                teacher = Teacher.objects.get(id=teacher_id)
                course = Courses.objects.get(id=course_id)
                class_period.teacher = teacher
                class_period.course = course
                class_period.save()
