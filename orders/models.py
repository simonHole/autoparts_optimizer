from django.db import models
from uuid import uuid4
from parts.models import Part

# Create your models here.


class Order(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True)
    part = models.ManyToManyField(Part)

    def __str__(self):
        return self.client

    def save(self, *args, **kwargs):
        super(Order, self).save(*args, **kwargs)

    @property
    def total_price(self):
        total_price = 0
        products = self.part.all()
        for product in products:
            total_price += product
        self.total_price = total_price
