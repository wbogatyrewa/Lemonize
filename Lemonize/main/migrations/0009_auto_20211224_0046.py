# Generated by Django 3.2.10 on 2021-12-23 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_order_total_sum'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='basket',
        ),
        migrations.AddField(
            model_name='order',
            name='basket',
            field=models.ManyToManyField(to='main.Basket'),
        ),
    ]
