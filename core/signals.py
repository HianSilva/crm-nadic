from django.db import transaction
from django.db.models import F
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from core.models import OrderItem, Revenue

MONTH_KEYS = {
    1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun',
    7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'
}

def _update_revenue_record(order_value, **lookup_filters):
    revenue, created = Revenue.objects.get_or_create(
        defaults={'value': 0},
        **lookup_filters
    )
    revenue.value += order_value
    revenue.save()

@receiver(post_save, sender=OrderItem)
@transaction.atomic
def handle_order_item_creation(sender, instance, created, **kwargs):
    """
    Após a criação de um OrderItem, atualiza a receita e reduz o estoque de forma atômica.
    """
    if not created:
        return

    sale_date = instance.created_at
    order_value = instance.total_price
    year = sale_date.year
    month_number = sale_date.month
    month_key = MONTH_KEYS[month_number]
    trimester = (month_number - 1) // 3 + 1
    semester = (month_number - 1) // 6 + 1

    _update_revenue_record(order_value, year=year, month=month_key)
    _update_revenue_record(order_value, year=year, trimester=trimester, month=None)
    _update_revenue_record(order_value, year=year, semester=semester, month=None)
    _update_revenue_record(order_value, year=year, month=None, trimester=None, semester=None)

    product = instance.product
    product.stock_quantity = F('stock_quantity') - instance.quantity
    product.save()


@receiver(pre_delete, sender=OrderItem)
@transaction.atomic
def decrease_revenue_on_sale_deletion(sender, instance, **kwargs):
    """
    Antes de um OrderItem ser deletado, DIMINUI a receita correspondente.
    """
    sale_date = instance.created_at
    order_value = -instance.total_price
    year = sale_date.year
    month_number = sale_date.month
    month_key = MONTH_KEYS[month_number]
    trimester = (month_number - 1) // 3 + 1
    semester = (month_number - 1) // 6 + 1

    _update_revenue_record(order_value, year=year, month=month_key)
    _update_revenue_record(order_value, year=year, trimester=trimester, month=None)
    _update_revenue_record(order_value, year=year, semester=semester, month=None)
    _update_revenue_record(order_value, year=year, month=None, trimester=None, semester=None)


@receiver(pre_delete, sender=OrderItem)
def restore_stock_on_sale_deletion(sender, instance, **kwargs):
    """
    Antes de um OrderItem ser deletado, RESTAURA o estoque correspondente.
    """
    product = instance.product
    product.stock_quantity = F('stock_quantity') + instance.quantity
    product.save()