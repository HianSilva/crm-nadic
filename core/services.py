from django.db import transaction
from .models import Order, OrderItem

@transaction.atomic
def create_order_with_items(customer, items_data):
    order = Order.objects.create(customer=customer)

    for item_data in items_data:
        product = item_data.get('product')
        quantity = item_data.get('quantity')

        if not product or not quantity:
            raise ValueError("Dados do item inválidos.")

        if quantity > product.stock_quantity:
            raise ValueError(
                f"Estoque insuficiente para o produto '{product.name}'. "
                f"Solicitado: {quantity}, Disponível: {product.stock_quantity}"
            )

    order_items_to_create = []
    for item_data in items_data:
        item_data.pop('id', None)
        item_data.pop('DELETE', None)

        order_items_to_create.append(
            OrderItem(order=order, **item_data)
        )

    OrderItem.objects.bulk_create(order_items_to_create)

    return order