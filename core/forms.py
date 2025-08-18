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

class BaseOrderItemFormSet(forms.BaseInlineFormSet):
    def clean(self):

        super().clean()

        # Itera sobre cada formulário no formset
        for form in self.forms:
            # Não faz nada se o formulário não tiver dados
            if not form.is_valid() or not form.cleaned_data:
                continue

            # Pega os dados validados do formulário
            product = form.cleaned_data.get('product')
            quantity = form.cleaned_data.get('quantity')

            # Se 'product' ou 'quantity' não estiverem presentes, pula a validação
            if not product or not quantity:
                continue

            # Verifica se a quantidade solicitada é maior que o estoque do produto
            if quantity > product.stock_quantity:
                form.add_error('quantity',
                               f'A quantidade solicitada ({quantity}) excede o estoque disponível ({product.stock}).')

OrderItemFormSet = forms.inlineformset_factory(
    Order,
    OrderItem,
    fields=('product', 'quantity', 'product_sale_price'),
    formset=BaseOrderItemFormSet,
    extra=1,
    can_delete=True
)