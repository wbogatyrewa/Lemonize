# Generated by Django 3.2.10 on 2021-12-23 20:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20211224_0046'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='basket',
        ),
    ]
