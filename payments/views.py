from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Payment
from .serializers import PaymentSerializer

class PaymentCreateView(generics.CreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
