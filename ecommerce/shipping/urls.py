from django.urls import path
from .views import ShippingAddressView

urlpatterns = [
    path('address/', ShippingAddressView.as_view(), name='shipping-address'),
]
