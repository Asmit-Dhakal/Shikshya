from django.db import models
from users.models import User
from courses.models import Course

class Review(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='reviews')
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField()
    comment = models.TextField()

    def __str__(self):
        return f'{self.course.title} review by {self.student.gmail}'
