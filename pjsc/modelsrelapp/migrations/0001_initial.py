# Generated by Django 2.1.15 on 2019-12-10 08:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'school',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('sex', models.CharField(max_length=10)),
                ('score', models.FloatField()),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stu', to='modelsrelapp.School')),
            ],
            options={
                'db_table': 'student1',
            },
        ),
    ]
