from django import forms
from django.core.validators import MinValueValidator
from .models import *

class ProductForm(forms.ModelForm):
    stock_quantity = forms.IntegerField(validators=[MinValueValidator(1)])

    class Meta:
        model = Product
        fields = ['name', 'price', 'stock_quantity']

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'email', 'phone']

class OrderForm(forms.ModelForm):
    customer = forms.ModelChoiceField(
        queryset=Customer.objects.all(),
        label='Cliente',
    )
    class Meta:
        model = Order
        fields = ['customer']

class OrderItemForm(forms.ModelForm):
    product = forms.ModelChoiceField(
        queryset=Product.objects.all(),
        label='Produto',
        empty_label="Selecione um produto"
    )
    quantity = forms.IntegerField(
        validators=[MinValueValidator(1)],
        label='Quantidade',
        widget=forms.NumberInput(attrs={'min': 1})
    )

    class Meta:
        model = OrderItem
        fields = ['product', 'quantity']

    def clean(self):
        cleaned_data = super().clean()
        product = cleaned_data.get('product')
        quantity = cleaned_data.get('quantity')

        if product and quantity:
            if quantity > product.stock_quantity:
                raise forms.ValidationError(
                    f'A quantidade solicitada ({quantity}) excede o estoque disponível ({product.stock_quantity}).'
                )

        return cleaned_data

OrderItemFormSet = forms.formset_factory(
    OrderItemForm,
    extra=1,
    can_delete=False,
    min_num=1,
    validate_min=True,
    max_num=10
)