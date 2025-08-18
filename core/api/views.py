from rest_framework import viewsets, generics
from rest_framework.permissions import DjangoModelPermissions

from core.models import Product, Revenue
from core.api.serializers import ProductSerializer, RevenueSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [DjangoModelPermissions]

class RevenueListView(generics.ListAPIView):
    queryset = Revenue.objects.all()
    serializer_class = RevenueSerializer
    permission_classes = [DjangoModelPermissions]