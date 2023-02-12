from django.contrib.auth.models import User
from .models import Client

from django.db.models.signals import post_save, post_delete


def create_client(sender, instance, created, **kwargs):
    if created:
        user = instance
        client = Client(
            user=user,
            username=user.username,
            email=user.email,
            name=user.first_name,
            surname=user.last_name
        )

        client.save()


def update_user(sender, instance, created, **kwargs):
    client = instance
    user = client.user

    if not created:
        user.first_name = client.name
        user.last_name = client.surname
        user.email = client.email
        user.save()


def delete_user(sender, instance, **kwargs):
    try:
        user = instance.user
        user.delete()
    except:
        pass


post_save.connect(create_client, sender=User)
post_save.connect(update_user, sender=Client)
post_delete.connect(delete_user, sender=Client)
