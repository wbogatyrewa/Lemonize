from django.db import models


class Product(models.Model):
    title = models.CharField('Название', max_length=50)
    type = models.CharField('Тип', max_length=50)
    price = models.IntegerField('Цена')
    image = models.TextField('Путь до фото')

    def __str__(self):
        return self.title


class Basket(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.IntegerField('Количество', default=1)
    total = models.IntegerField('Итого', default=0, )

    def __str__(self):
        return ''