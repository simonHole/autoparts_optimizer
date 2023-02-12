from django.db import models
from uuid import uuid4

from parts.models import Part
from users.models import Client

# Create your models here.


class Order(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True,
                          unique=True, editable=False)
    client = models.ForeignKey(
        Client, on_delete=models.SET_NULL, null=True, blank=True)
    transaction = models.CharField(max_length=200, null=True, blank=False)
    order_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    complete = models.BooleanField(default=False, null=True, blank=False)

    def __str__(self):
        return f'{self.client.name} {self.client.surname} - {self.order_date} - {self.complete}'

    @property
    def latest_delivery_days(self):
        order_items = self.orderitem_set.all()
        latest = max([item.part.time_of_delivery for item in order_items])
        return latest

    @property
    def cart_total(self):
        order_items = self.orderitem_set.all()
        total = sum([item.total for item in order_items])
        return total

    @property
    def cart_items(self):
        order_items = self.orderitem_set.all()
        total = sum([item.quantity for item in order_items])
        return total


class OrderItem(models.Model):
    part = models.ForeignKey(
        Part, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(
        Order, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    addition_date = models.DateTimeField(
        auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f'{self.part.name} - {self.order}'

    @property
    def total(self):
        total_price = self.part.price * self.quantity
        return total_price


class ShipAddress(models.Model):
    customer = models.ForeignKey(
        Client, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(
        Order, on_delete=models.SET_NULL, null=True, blank=True)
    city = models.CharField(max_length=200, null=True)
    zipcode = models.CharField(max_length=200, null=True, blank=False)
    address = models.CharField(max_length=200, null=True, blank=False)
    apartament = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return f'{self.zipcode} {self.city} - {self.address}'
