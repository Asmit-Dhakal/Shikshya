from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import User

class StudentRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['email', 'password', 'password2', 'first_name', 'last_name', 'address', 'country']
        extra_kwargs = {
            'password': {'write_only': True},
            'password2': {'write_only': True},
        }

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError({'password': 'Passwords must match.'})
        return data

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create_user(
            email=validated_data['email'],
            password=password,
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            address=validated_data['address'],
            country=validated_data['country'],
            is_student=True
        )
        return user

class StudentLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        # Check if the email exists in the database
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError('Gmail not found.')

        # Authenticate the user
        user = authenticate(email=email, password=password)
        if user is None:
            raise serializers.ValidationError('Password incorrect.')

        if not user.is_student:
            raise serializers.ValidationError('User is not registered as a student.')

        return {'user': user}
# users/serializers.py

class TeacherRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['email', 'password', 'password2', 'first_name', 'last_name', 'address', 'country']
        extra_kwargs = {
            'password': {'write_only': True},
            'password2': {'write_only': True},
        }

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError({'password': 'Passwords must match.'})
        return data

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create_user(
            email=validated_data['email'],
            password=password,
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            address=validated_data['address'],
            country=validated_data['country'],
            is_teacher=True
        )
        return user

class TeacherLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        # Check if the email exists in the database
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError('Gmail not found.')

        # Authenticate the user
        user = authenticate(email=email, password=password)
        if user is None:
            raise serializers.ValidationError('Password incorrect.')

        if not user.is_teacher:
            raise serializers.ValidationError('User is not registered as a teacher.')

        return {'user': user}