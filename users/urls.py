from django.urls import path
from .views import RegisterStudent, RegisterTeacher, LoginStudent, LoginTeacher

urlpatterns = [
    path('register/student/', RegisterStudent.as_view(), name='register-student'),
    path('register/teacher/', RegisterTeacher.as_view(), name='register-teacher'),
    path('login/student/', LoginStudent.as_view(), name='login-student'),
    path('login/teacher/', LoginTeacher.as_view(), name='login-teacher'),
]
