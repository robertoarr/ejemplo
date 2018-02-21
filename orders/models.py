from django.db import models


class Order(models.Model):
    ONE = 'BE'
    TWO = 'PL'
    THREE = 'HU'
    STATUS_CHOICES = (
        (ONE, 'bee'),
        (TWO, 'plant'),
        (THREE, 'human'),
    )
    customer = models.ForeignKey('users.Customer', related_name='order', on_delete=models.SET_NULL, null=True)
    order_date = models.DateTimeField(editable=False, auto_now_add=True)
    shipped_date = models.DateTimeField(null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    comments = models.CharField(max_length=400, default='', blank=True)
    order_detail = models.ManyToManyField(
        'orders.Product',
        through='OrderDetail',
        through_fields=('order', 'product'),
    )


class OrderDetail(models.Model):
    order = models.ForeignKey('orders.Order', on_delete=models.CASCADE)
    product = models.ForeignKey('orders.Product', on_delete=models.CASCADE)


class Product(models.Model):
    product_line = models.ForeignKey('orders.ProductLine',
                                     related_name='product',
                                     on_delete=models.SET_NULL,
                                     null=True)
    name = models.CharField(max_length=20, null=False)
    description = models.CharField(max_length=400, null=False, blank=True, default='')
    price = models.IntegerField(null=False)
    stock = models.IntegerField(null=False)


class ProductLine(models.Model):
    description = models.CharField(max_length=400, null=False, blank=True, default='')
    web_page = models.URLField(blank=True, default='')
