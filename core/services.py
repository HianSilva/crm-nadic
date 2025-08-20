from django.db import transaction
from .models import Order, OrderItem

@transaction.atomic
def create_order_with_items(customer, items_data):
    """
    Creates an order with associated items.
    Stock validation and updates are handled by signals.
    """
    if not items_data:
        raise ValueError("Pelo menos um item deve ser adicionado ao pedido.")
    
    order = Order.objects.create(customer=customer)

    order_items_to_create = []
    for item_data in items_data:
        product = item_data.get('product')
        quantity = item_data.get('quantity')

        if not product or not quantity:
            raise ValueError("Dados do item inválidos.")
        
        OrderItem.objects.create(
            order=order,
            product=product,
            quantity=quantity
        )

    return order