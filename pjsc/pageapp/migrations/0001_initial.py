# Generated by Django 2.1.15 on 2019-12-18 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Xues',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('score', models.FloatField()),
                ('sex', models.CharField(max_length=5)),
            ],
            options={
                'db_table': 'xuesheng',
            },
        ),
    ]
