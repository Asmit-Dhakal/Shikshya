from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import StudentSerializer, TeacherSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate

class RegisterStudent(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = StudentSerializer

    def perform_create(self, serializer):
        serializer.save(is_student=True)

class RegisterTeacher(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = TeacherSerializer

    def perform_create(self, serializer):
        serializer.save(is_teacher=True)

class LoginStudent(generics.GenericAPIView):
    def post(self, request):
        gmail = request.data.get('gmail')
        password = request.data.get('password')
        user = authenticate(gmail=gmail, password=password)
        if user and user.is_student:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        return Response({'error': 'Invalid credentials or not a student'}, status=status.HTTP_400_BAD_REQUEST)

class LoginTeacher(generics.GenericAPIView):
    def post(self, request):
        gmail = request.data.get('gmail')
        password = request.data.get('password')
        user = authenticate(gmail=gmail, password=password)
        if user and user.is_teacher:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        return Response({'error': 'Invalid credentials or not a teacher'}, status=status.HTTP_400_BAD_REQUEST)
