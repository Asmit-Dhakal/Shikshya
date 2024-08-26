from django.urls import path
from .views import PaymentCreateView

urlpatterns = [
    path('payments/', PaymentCreateView.as_view(), name='payment-create'),
]
