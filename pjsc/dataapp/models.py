from django.db import models


class Fruit(models.Model):
    name = models.CharField(max_length=20)  # 模型类属性对应得表的字段
    price = models.FloatField()
    color = models.CharField(max_length=20)
    # image = models.ImageField()

    class Meta:
        db_table = 'Fruit'


class Student(models.Model):
    name = models.CharField(max_length=20)
    sex = models.CharField(max_length=5)
    score = models.FloatField()
    birthday = models.DateField(default='1998-01-01')

    class Meta:
        db_table = 'student'
