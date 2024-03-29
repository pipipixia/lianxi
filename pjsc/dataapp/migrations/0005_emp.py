# Generated by Django 2.1.15 on 2019-12-07 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataapp', '0004_auto_20191206_1615'),
    ]

    operations = [
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('sex', models.CharField(max_length=5)),
                ('salary', models.FloatField()),
                ('is_married', models.BooleanField()),
            ],
            options={
                'db_table': 'emp',
            },
        ),
    ]
