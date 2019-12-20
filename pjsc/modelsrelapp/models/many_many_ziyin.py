from django.db import models


class Weiuser(models.Model):
    username = models.CharField(max_length=20)
    sex = models.CharField(max_length=5)

    class Meta:
        db_table = 'weiuser'


class relation(models.Model):
    follwed = models.ForeignKey(Weiuser, on_delete=models.CASCADE, related_name='fanns_user')  # ±»¹Ø×¢×Å
    fans = models.ForeignKey(Weiuser, on_delete=models.CASCADE, related_name='follwed_user')  # ·ÛË¿
    built_time = models.DateField(null=True)

    class Meta:
        db_table = 'relation'
