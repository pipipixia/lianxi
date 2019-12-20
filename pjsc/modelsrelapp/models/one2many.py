from django.db import models


class School(models.Model): # һ��ģ��
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=30)

    class Meta:
        db_table = 'school'


class Student(models.Model): # ���෽ģ�͡�
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    sex = models.CharField(max_length=10)
    score = models.FloatField()
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='stu') # �������������һ����ģ��

    class Meta:
        db_table = 'student1'
