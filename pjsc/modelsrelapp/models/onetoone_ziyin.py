from django.db import models


class Spy(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    sex = models.CharField(max_length=5)
    manager = models.OneToOneField('self', on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'spies'
