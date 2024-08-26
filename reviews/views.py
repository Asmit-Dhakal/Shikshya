from rest_framework import generics
from .models import Review
from .serializers import ReviewSerializer

class ReviewListCreate(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
