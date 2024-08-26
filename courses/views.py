from rest_framework import generics, permissions
from rest_framework.exceptions import PermissionDenied
from .models import Course
from .serializers import CourseSerializer

class CourseListCreate(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        if not self.request.user.is_teacher:
            raise PermissionDenied("Only teachers can create courses.")
        serializer.save(teacher=self.request.user)

class CourseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        course = self.get_object()
        if self.request.user != course.teacher:
            raise PermissionDenied("Only the teacher who created the course can update it.")
        serializer.save()
