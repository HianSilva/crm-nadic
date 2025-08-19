from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)
    price = models.FloatField()
    stock_quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.name} - {self.price} - {self.stock_quantity}'

class Customer(models.Model):
    name = models.CharField(max_length=100, unique=True)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Order(models.Model):
    datetime = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    @property
    def total_price(self):
        return sum(item.total_price for item in self.orderitem_set.all())

    def __str__(self):
        return f'{self.customer.name} - {self.datetime} - {self.total_price}'

class OrderItem(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    product_sale_price = models.FloatField()

    @property
    def total_price(self):
        return self.product_sale_price * self.quantity

    def __str__(self):
        return f'{self.product.name} - {self.quantity}'

class Revenue(models.Model):
    MONTH_CHOICES = (
        ('Jan', 'Janeiro'),
        ('Feb', 'Fevereiro'),
        ('Mar', 'Março'),
        ('Apr', 'Abril'),
        ('May', 'Maio'),
        ('Jun', 'Junho'),
        ('Jul', 'Julho'),
        ('Aug', 'Agosto'),
        ('Sep', 'Setembro'),
        ('Oct', 'Outubro'),
        ('Nov', 'Novembro'),
        ('Dec', 'Dezembro')
    )

    updated_at = models.DateTimeField(auto_now=True)
    value = models.FloatField()
    month = models.CharField(max_length=10, choices=MONTH_CHOICES, null=True, blank=True)
    year = models.IntegerField()
    semester = models.IntegerField(null=True, blank=True)
    trimester = models.IntegerField(null=True, blank=True)

    @property
    def time_period(self):
        time_period = ""
        if self.semester:
            time_period = f'{self.semester}° Semestre de {self.year}'
        elif self.trimester:
            time_period = f'{self.trimester}° Trimestre de {self.year}'
        elif self.month:
            time_period = f'{self.month} de {self.year}'

        time_period = f'{time_period} (Atualizado em {self.updated_at})'

        return time_period


    def __str__(self):
        return f'{self.time_period}'
