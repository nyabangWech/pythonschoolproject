from django.urls import path
from .views import studentListView
urlpatterns=[
    path("student/",studentListView.as_view(),name="student_list_view")
]