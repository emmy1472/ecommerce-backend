from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ShippingAddress
from .serializers import ShippingAddressSerializer

class ShippingAddressView(APIView):
    def post(self, request):
        serializer = ShippingAddressSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, order_id):
        try:
            shipping_address = ShippingAddress.objects.get(order_id=order_id)
            serializer = ShippingAddressSerializer(shipping_address)
            return Response(serializer.data)
        except ShippingAddress.DoesNotExist:
            return Response({'error': 'Shipping address not found'}, status=status.HTTP_404_NOT_FOUND)
