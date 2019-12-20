from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=20, unique=True)
    age = models.IntegerField()
    sex = models.CharField(max_length=5)

    class Meta:
        db_table = 'person'


class Card(models.Model):  # ���֤ģ��
    cardno = models.CharField(primary_key=True, max_length=20)  # ����
    color = models.CharField(max_length=10)
    person = models.OneToOneField(Person, on_delete=models.CASCADE, related_name='yourcard')

    class Meta:
        db_table = 'card'
