from django.db import models


class School(models.Model): # 一方模型
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=30)

    class Meta:
        db_table = 'school'


class Student(models.Model): # ‘多方模型’
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    sex = models.CharField(max_length=10)
    score = models.FloatField()
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='stu') # 设置外键关联‘一方’模型

    class Meta:
        db_table = 'student1'
