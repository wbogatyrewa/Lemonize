from django.db import models


class Product(models.Model):
    title = models.CharField('Название', max_length=50)
    type = models.CharField('Тип', max_length=50)
    price = models.IntegerField('Цена')
    image = models.TextField('Путь до фото')

    def __str__(self):
        return self.title

    def __eq__(self, other):
        return self.title == other.title


class Basket(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.IntegerField('Количество', default=1)

    def __str__(self):
        return self.product_id.title + ' ' + str(self.count) + ' шт.'


class Order(models.Model):
    basket = models.ManyToManyField(Basket)
    name = models.CharField('ФИО', max_length=255)
    phone = models.IntegerField('Телефон')
    delivery = models.CharField('Способ доставки', max_length=50)
    total_sum = models.IntegerField('Итоговая сумма', default=0)

    def __str__(self):
        return self.name