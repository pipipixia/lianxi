from django.db import models


class User(models.Model):
    user = models.CharField(max_length=10)
    password = models.CharField(max_length=100)

    class Meta:
        db_table = 'user'


class Image(models.Model):
    image_id = models.IntegerField()
    path = models.CharField(max_length=30,null=False)

