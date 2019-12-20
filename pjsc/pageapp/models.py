from django.db import models

class Xues(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    score = models.FloatField()
    sex = models.CharField(max_length=5)

    class Meta:
        db_table = 'xuesheng'
