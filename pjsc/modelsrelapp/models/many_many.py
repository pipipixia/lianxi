from django.db import models


class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    sex = models.CharField(max_length=10)

    class Meta:
        db_table = 'user'


class Group(models.Model):  # ×éÄ£ÐÍ
    gruopname = models.CharField(max_length=20)
    users = models.ManyToManyField(User, related_name='yourgroup')

    class Meta:
        db_table = 'groups'
