import uuid
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class extenduser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    apikey = models.CharField(max_length=36, default=uuid.uuid4, unique='True')

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_extenduser(sender, instance, created, **kwargs):
    if created:
        extenduser.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_extenduser(sender, instance, **kwargs):
    instance.extenduser.save()
