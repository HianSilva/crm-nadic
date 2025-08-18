from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View

from core.forms import ProductForm, OrderForm, OrderItemFormSet, CustomerForm
from core.models import Product, Order, Customer, Revenue
from core.services import create_order_with_items


# Products Views
class ProductListView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'products/products_list.html'

class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'products/product_detail.html'
    slug_url_kwarg = 'slug'
    slug_field = 'name'

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/new_product.html'
    success_url = reverse_lazy('products-list')

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/product_update.html'
    success_url = reverse_lazy('products-list')
    slug_url_kwarg = 'slug'
    slug_field = 'name'

class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('products-list')
    slug_url_kwarg = 'slug'
    slug_field = 'name'

# Orders Views
class OrderCreateView(View):
    template_name = 'orders/sale_page.html'
    success_url = reverse_lazy('orders-list')

    def get(self, request, *args, **kwargs):
            order_form = OrderForm()
            items_formset = OrderItemFormSet(prefix='items')

            context = {
                'order_form': order_form,
                'items_formset': items_formset,
            }

            return render(request, self.template_name, context=context)

    def post(self, request, *args, **kwargs):
        order_form = OrderForm(data=request.POST)
        items_formset = OrderItemFormSet(data=request.POST)

        if order_form.is_valid() and items_formset.is_valid():
            try:
                customer = order_form.cleaned_data['customer']
                items = items_formset.cleaned_data

                create_order_with_items(customer, items)

                return redirect(self.success_url)

            except ValueError as e:
                items_formset.add_error(None, str(e))

        context = {
            'order_form': order_form,
            'items_formset': items_formset,
        }
        return render(request, self.template_name, context)

class OrderListView(ListView):
    model = Order
    context_object_name = 'orders'
    template_name = 'orders/orders_list.html'

class OrderDetailView(DetailView):
    model = Order
    context_object_name = 'order'
    template_name = 'orders/order_detail.html'

class OrderDeleteView(DeleteView):
    model = Order
    success_url = reverse_lazy('orders-list')

# Customers Views
class CustomersListView(ListView):
    model = Customer
    context_object_name = 'Customers'
    template_name = 'customers/customers_list.html'

class CustomerDetailView(DetailView):
    model = Customer
    context_object_name = 'Customer'
    slug_url_kwarg = 'slug'
    slug_field = 'name'
    template_name = 'customers/customer_detail.html'
    form_class = CustomerForm

class CustomerCreateView(CreateView):
    model = Customer
    context_object_name = 'Customer'
    template_name = 'customers/create_customer.html'
    form_class = CustomerForm
    success_url = reverse_lazy('customers-list')

class CustomerUpdateView(UpdateView):
    model = Customer
    template_name = 'customers/customer_update.html'
    slug_url_kwarg = 'slug'
    slug_field = 'name'
    success_url = reverse_lazy('customers-list')
    form_class = CustomerForm

class CustomerDeleteView(DeleteView):
    model = Customer
    slug_url_kwarg = 'slug'
    slug_field = 'name'
    success_url = reverse_lazy('customers-list')

# Revenues Views
class RevenueListView(ListView):
    model = Revenue
    context_object_name = 'revenues'
    template_name = 'revenues/revenues_list.html'