from django.urls import path
from .views import StudentListView
from .views import ClassroomListView
from .views import ClassesListView
from .views import CourseListView
from .views import TeacherListView
from .views import StudentDetailView
from .views import courseDetailView
from .views import classroomDetailView
from .views import classesDetailView
from .views import teacherDetailView
from .views import assign_teacher_to_course




urlpatterns=[
    path("student/",StudentListView.as_view(),name="student_list_view"),
    path("teacher/",TeacherListView.as_view(),name="teacher_list_view"),
    path("classroom/",ClassroomListView.as_view(),name="classroom_list_view"),
    path("classes/",ClassesListView.as_view(),name="classes_list_view"),
    path("course/",CourseListView.as_view(),name="course_list_view"),
    path("student/<int:id>/",StudentDetailView.as_view(),name="student_detail_view"),
    path("course/<int:id>/",courseDetailView.as_view(),name="Course_detail_view"),
    path("classroom/<int:id>/",classroomDetailView.as_view(),name="Course_detail_view"),
    path("classes/<int:id>/",classesDetailView.as_view(),name="Course_detail_view"),
    path("teacher/<int:id>/",teacherDetailView.as_view(),name="Course_detail_view"),
    path('courses/<int:course_id>/assign-teacher/', assign_teacher_to_course, name='assign_teacher_to_course'),
    



      
]







