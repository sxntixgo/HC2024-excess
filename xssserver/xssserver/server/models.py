from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse

from datetime import datetime, timezone
import uuid

class GameUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    last_check = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return "{user}".format(user=self.user)

@receiver(post_save, sender=User)
def create_gameuser(sender, instance, created, **kwargs):
    if created:
        GameUser.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_gameuser(sender, instance, **kwargs):
    instance.gameuser.save()

class TargetServer(models.Model):
    name = models.CharField(max_length=64)
    url = models.URLField(max_length=256)
    flag = models.CharField(max_length=64)

    def __str__(self):
        return self.name

class Attempt(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    target_server = models.ForeignKey(TargetServer, on_delete=models.CASCADE, null=True)
    resource_and_query_string = models.CharField(max_length=2048, null=True, blank=True)
    datetime = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    result = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse("attempt_detail", kwargs={"pk": self.pk})