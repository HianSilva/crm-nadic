from django.urls import path, include
from rest_framework import routers
from core.api.views import ProductViewSet, RevenueListView

router = routers.DefaultRouter()

router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('revenues/', RevenueListView.as_view(), name='revenues'),
]