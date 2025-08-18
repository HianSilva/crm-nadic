from django.urls import path
from core.views import *

urlpatterns = [
    # Products urls
    path('products', ProductListView.as_view(), name='products-list'),
    path('products/<slug:slug>', ProductDetailView.as_view(), name='product-detail'),
    path('products/create', ProductCreateView.as_view(), name='product-create'),
    path('products/<slug:slug>/update', ProductUpdateView.as_view(), name='product-update'),
    path('products/<slug:slug>/delete', ProductDeleteView.as_view(), name='product-delete'),
    # Orders urls
    path('orders', OrderListView.as_view(), name='orders_list'),
    path('orders/<int:pk>', OrderDetailView.as_view(), name='order-detail'),
    path('orders/<int:pk>/delete', OrderDeleteView.as_view(), name='order-delete'),
    path('orders/create', OrderCreateView.as_view(), name='order-create'),
    # Customers
    path('customers', CustomersListView.as_view(), name='customers_list'),
    path('customers/<int:pk>', CustomerDetailView.as_view(), name='customer-detail'),
    path('customers/create', CustomerCreateView.as_view(), name='customer-create'),
    path('customers/<slug:slug>/update', CustomerUpdateView.as_view(), name='customer-update'),
    path('customers/<slug:slug>/delete', CustomerDeleteView.as_view(), name='customer-delete'),
]