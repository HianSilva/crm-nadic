from django.urls import path
from core.views import *

urlpatterns = [
    # Products urls
    path('', ProductListView.as_view(), name='products-list'),
    path('products/create/', ProductCreateView.as_view(), name='product-create'),
    path('products/<slug:slug>/', ProductDetailView.as_view(), name='product-detail'),
    path('products/<slug:slug>/update/', ProductUpdateView.as_view(), name='product-update'),
    path('products/<slug:slug>/delete/', ProductDeleteView.as_view(), name='product-delete'),
    # Orders urls
    path('orders/', OrderListView.as_view(), name='orders-list'),
    path('orders/create/', OrderCreateView.as_view(), name='order-create'),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
    path('orders/<int:pk>/delete/', OrderDeleteView.as_view(), name='order-delete'),
    # Customers
    path('customers/', CustomersListView.as_view(), name='customers-list'),
    path('customers/create/', CustomerCreateView.as_view(), name='customer-create'),
    path('customers/<slug:slug>', CustomerDetailView.as_view(), name='customer-detail'),
    path('customers/<slug:slug>/update/', CustomerUpdateView.as_view(), name='customer-update'),
    path('customers/<slug:slug>/delete/', CustomerDeleteView.as_view(), name='customer-delete'),
    # Revenues
    path('revenues/', RevenueListView.as_view(), name='revenues-list')
]