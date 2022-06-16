import json

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models

from .choices import *

user = settings.AUTH_USER_MODEL


class User(AbstractUser):
    bio = models.TextField(blank=True)


class LGPDPermissions(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(user, on_delete=models.CASCADE)
    name_permission = models.BooleanField(default=True, blank=True)
    email_permission = models.BooleanField(default=True, blank=True)
    bio_permission = models.BooleanField(default=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class FormAttention(models.Model):
    user = models.OneToOneField(user, on_delete=models.CASCADE)
    questao1 = models.CharField(
        max_length=1, choices=QUESTAO_4_CHOICES, blank=False, null=False
    )
    questao2 = models.CharField(
        max_length=1, choices=QUESTAO_4_CHOICES, blank=False, null=False
    )
    questao3 = models.CharField(
        max_length=1, choices=QUESTAO_4_CHOICES, blank=False, null=False
    )
    questao4 = models.CharField(
        max_length=1, choices=QUESTAO_4_CHOICES, blank=False, null=False
    )
    questao5 = models.CharField(
        max_length=1, choices=QUESTAO_4_CHOICES, blank=False, null=False
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return json.dumps(
            {
                "user": self.user.username,
                "questao1": self.questao1,
                "questao2": self.questao2,
                "questao3": self.questao3,
                "questao4": self.questao4,
                "questao5": self.questao5,
            }
        )


class FormPersonality(models.Model):
    user = models.OneToOneField(user, on_delete=models.CASCADE)
    questao1 = models.CharField(
        max_length=1, choices=QUESTAO_5_CHOICES, blank=False, null=False
    )
    questao2 = models.CharField(
        max_length=1, choices=QUESTAO_5_CHOICES, blank=False, null=False
    )
    questao3 = models.CharField(
        max_length=1, choices=QUESTAO_5_CHOICES, blank=False, null=False
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return json.dumps(
            {
                "user": self.user.username,
                "questao1": self.questao1,
                "questao2": self.questao2,
                "questao3": self.questao3,
            }
        )


class FormLearning(models.Model):
    user = models.OneToOneField(user, on_delete=models.CASCADE)
    questao1 = models.CharField(
        max_length=1, choices=QUESTAO_6_CHOICES, blank=False, null=False
    )
    questao2 = models.CharField(
        max_length=1, choices=QUESTAO_6_CHOICES, blank=False, null=False
    )
    questao3 = models.CharField(
        max_length=1, choices=QUESTAO_6_CHOICES, blank=False, null=False
    )
    questao4 = models.CharField(
        max_length=1, choices=QUESTAO_6_CHOICES, blank=False, null=False
    )
    questao5 = models.CharField(
        max_length=1, choices=QUESTAO_6_CHOICES, blank=False, null=False
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return json.dumps(
            {
                "user": self.user.username,
                "questao1": self.questao1,
                "questao2": self.questao2,
                "questao3": self.questao3,
                "questao6": self.questao6,
                "questao5": self.questao5,
            }
        )
