# Generated by Django 2.1.15 on 2019-12-13 09:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pi_jie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shp_id', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('extend', models.CharField(max_length=5)),
            ],
            options={
                'db_table': 'pj_sc',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=50)),
                ('huoz_id', models.IntegerField()),
            ],
            options={
                'db_table': 'users',
            },
        ),
        migrations.AddField(
            model_name='pi_jie',
            name='huozhu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.User'),
        ),
    ]
