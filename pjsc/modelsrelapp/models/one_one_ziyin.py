from django.db import models


class Emp(models.Model):
    name = models.CharField(max_length=10)
    age = models.IntegerField()
    sex = models.CharField(max_length=5)
    salary = models.FloatField()
    manager = models.ForeignKey('self', on_delete=models.CASCADE, null=True)  # ��������

    class Meta:
        db_table = 'emp'
