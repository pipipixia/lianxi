# Generated by Django 2.1.15 on 2019-12-06 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataapp', '0002_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='birthday',
            field=models.DateField(null=True),
        ),
    ]
