from django.urls import path, include
from .views import ProductListView, ProductDetailView
from django.conf import settings
from django.conf.urls.static import static
# from rest_framework.routers import DefaultRouter
# from .views import ProductViewSet

# router = DefaultRouter()
# router.register(r'products', ProductViewSet)





urlpatterns = [
    # path('api/', include(router.urls)),
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
