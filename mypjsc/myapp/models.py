from django.db import models


class User(models.Model):
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=50)
    huoz_id = models.IntegerField()

    class Meta:
        db_table = 'users'


class Pi_jie(models.Model):
    shp_id = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    extend = models.CharField(max_length=5)
    huozhu = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'pj_sc'