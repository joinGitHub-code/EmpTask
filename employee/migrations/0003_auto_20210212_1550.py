# Generated by Django 3.0.2 on 2021-02-12 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_auto_20210212_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
