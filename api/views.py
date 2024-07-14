# from django.shortcuts import render

from rest_framework.response import Response
from  rest_framework.views import APIView
from  student.models import Student
from .serializers import  studentserializers

class studentListView(APIView):
    def get(self,request):
        Student=Student.objects.all
        serializer=studentserializers(Student,many=True)
        return Response(serializer.data)
