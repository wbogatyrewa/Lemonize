# Generated by Django 3.2.10 on 2021-12-23 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='total_sum',
            field=models.IntegerField(default=0, verbose_name='Итоговая сумма'),
        ),
    ]
