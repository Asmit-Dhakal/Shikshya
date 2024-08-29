# users/urls.py

from django.urls import path
from .views import (
    StudentRegisterAPIView, StudentLoginAPIView,
    TeacherRegisterAPIView, TeacherLoginAPIView
)

urlpatterns = [
    path('register/student/', StudentRegisterAPIView.as_view(), name='student-register'),
    path('login/student/', StudentLoginAPIView.as_view(), name='student-login'),
    path('register/teacher/', TeacherRegisterAPIView.as_view(), name='teacher-register'),
    path('login/teacher/', TeacherLoginAPIView.as_view(), name='teacher-login'),
]
