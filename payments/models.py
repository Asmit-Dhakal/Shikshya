# payments/models.py
from django.db import models
from django.utils import timezone
from users.models import User
from courses.models import Course

class Payment(models.Model):
    PAYMENT_STATUS_CHOICES = [
        ('succeeded', 'Succeeded'),
        ('failed', 'Failed'),
        ('pending', 'Pending'),
    ]

    student = models.ForeignKey(User, related_name='payments', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, related_name='payments', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    paid_at = models.DateTimeField(auto_now_add=True)
    stripe_charge_id = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=20, choices=PAYMENT_STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"Payment of {self.amount} by {self.student} for {self.course}"
