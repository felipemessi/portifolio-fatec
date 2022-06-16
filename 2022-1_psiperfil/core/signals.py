from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from .models import LGPDPermissions, User


@receiver(post_save, sender=User, dispatch_uid="user.create_user")
def create_lgpdpermissions(sender, instance, created, **kwargs):
    if created:
        LGPDPermissions.objects.create(user=instance)


@receiver(post_save, sender=User, dispatch_uid="user.create_user")
def save_lgpdpermissions(sender, instance, **kwargs):
    instance.LGPDPermissions.save()
