from rest_framework import serializers
from .models import User

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'gmail', 'is_student']

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'gmail', 'is_teacher']
