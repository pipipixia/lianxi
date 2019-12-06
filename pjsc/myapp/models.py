from django.db import models

# Create your models here.
from django.http import HttpResponse


class User(models.Model):
    user = models.CharField(max_length=20)
    password = models.CharField(max_length=100)

    class Meta:
        db_table = 'users'
