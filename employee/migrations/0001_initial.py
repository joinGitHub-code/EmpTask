# Generated by Django 3.0.2 on 2021-02-12 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_name', models.CharField(max_length=25)),
                ('task', models.CharField(max_length=225)),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
