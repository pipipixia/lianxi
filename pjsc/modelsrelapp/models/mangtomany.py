from django.db import models


class Member(models.Model):  # ��Աģ��
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    sex = models.CharField(max_length=5)

    class Meta:
        db_table = 'membber'


class Community(models.Model):  # ����ģ��
    name = models.CharField(max_length=20)
    members = models.ManyToManyField(Member, through='Relationship')

    class Meta:
        db_table = 'communries'


class Relationship(models.Model):  # ��������ϵģ��ģ��
    member = models.ForeignKey(Member, on_delete=models.CASCADE)  # ��������ԣ�����Memeber����
    community = models.ForeignKey(Community, on_delete=models.CASCADE)  # ��������ԡ�����Community
    jion_date = models.DateField(null=True)
    join_reason = models.CharField(max_length=100)

    class Meta:
        db_table = 'relationships'