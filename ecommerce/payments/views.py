from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Payment
from .serializers import PaymentSerializer
from orders.models import Order  # Assuming an order model is related to payments

class PaymentView(APIView):
    def post(self, request):
        """
        Process a payment for an order.
        """
        data = request.data
        try:
            # Validate the order exists
            order_id = data.get("order")
            order = Order.objects.get(id=order_id)

            # Ensure the order is not already paid
            if order.status == "Paid":
                return Response({"error": "This order is already paid."}, status=status.HTTP_400_BAD_REQUEST)

            # Save the payment
            serializer = PaymentSerializer(data=data)
            if serializer.is_valid():
                payment = serializer.save()

                # Update the order status to 'Paid'
                order.status = "Paid"
                order.save()

                return Response(
                    {"message": "Payment processed successfully.", "payment": serializer.data},
                    status=status.HTTP_201_CREATED,
                )
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Order.DoesNotExist:
            return Response({"error": "Order not found."}, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, order_id):
        """
        Retrieve the payment details for a specific order.
        """
        try:
            payment = Payment.objects.get(order_id=order_id)
            serializer = PaymentSerializer(payment)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Payment.DoesNotExist:
            return Response({"error": "Payment for this order not found."}, status=status.HTTP_404_NOT_FOUND)
