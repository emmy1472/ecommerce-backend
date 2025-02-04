from django.urls import path
from .views import PaymentView

urlpatterns = [
    path('process/', PaymentView.as_view(), name='payment-process'),
    path('<int:order_id>/', PaymentView.as_view(), name='payment-detail'),
]
