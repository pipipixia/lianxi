from django.db import models


class Member(models.Model):  # 成员模型
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    sex = models.CharField(max_length=5)

    class Meta:
        db_table = 'membber'


class Community(models.Model):  # 社区模型
    name = models.CharField(max_length=20)
    members = models.ManyToManyField(Member, through='Relationship')

    class Meta:
        db_table = 'communries'


class Relationship(models.Model):  # 第三方关系模型模型
    member = models.ForeignKey(Member, on_delete=models.CASCADE)  # 外键类属性，关联Memeber属性
    community = models.ForeignKey(Community, on_delete=models.CASCADE)  # 外键类属性。关联Community
    jion_date = models.DateField(null=True)
    join_reason = models.CharField(max_length=100)

    class Meta:
        db_table = 'relationships'