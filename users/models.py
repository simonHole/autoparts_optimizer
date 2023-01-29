from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4

# Create your models here.


class Client(models.Model):
    id = models.UUIDField(default=uuid4, unique=True,
                          primary_key=True, editable=False)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    username = models.CharField(
        max_length=200, null=True, blank=True, unique=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    surname = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(
        max_length=500, null=True, blank=True, unique=True)
    location = models.CharField(max_length=500, null=True, blank=True)
    image = models.ImageField(
        null=True, blank=True, upload_to='parts/', default='profiles/user-placeholder.png')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} {self.surname} - {self.email}'
