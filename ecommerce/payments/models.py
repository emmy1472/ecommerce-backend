from django.db import models
from orders.models import Order  # Assuming orders are linked

class Payment(models.Model):
    PAYMENT_METHODS = [
        ('Card', 'Card'),
        ('BankTransfer', 'Bank Transfer'),
        ('PayPal', 'PayPal'),
    ]
    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name="payment")
    transaction_id = models.CharField(max_length=100, unique=True)
    payment_method = models.CharField(max_length=50, choices=PAYMENT_METHODS)
    status = models.CharField(max_length=50, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment for Order {self.order.id} - {self.transaction_id}"
