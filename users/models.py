from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils import timezone

class UserManager(BaseUserManager):
    def create_user(self, gmail, password=None, **extra_fields):
        if not gmail:
            raise ValueError('The Email field must be set')
        user = self.model(gmail=gmail, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, gmail, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(gmail, password, **extra_fields)

class User(AbstractBaseUser):
    gmail = models.EmailField(unique=True)
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'gmail'
    REQUIRED_FIELDS = []
