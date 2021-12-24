from django.shortcuts import render
from .models import Product, Basket, Order
import logging

logger = logging.getLogger(__name__)


def MainPage(request):
    logger.error('Загрузка главной страницы')
    return render(request, 'main/MainPage.html')


def ProductPagePastries(request):
    title = 'Пирожные'
    products = Product.objects.filter(type=title)
    add_to_basket(request)
    logger.error('Загрузка страницы пирожных')
    return render(request, 'main/ProductPage.html', {'title': title, 'products': products})


def ProductPageCakes(request):
    title = 'Торты'
    products = Product.objects.filter(type=title)
    add_to_basket(request)
    logger.error('Загрузка страницы тортов')
    return render(request, 'main/ProductPage.html', {'title': title, 'products': products})


def ProductPageMacaroons(request):
    title = 'Макаруны'
    products = Product.objects.filter(type=title)
    add_to_basket(request)
    logger.error('Загрузка страницы макарун')
    return render(request, 'main/ProductPage.html', {'title': title, 'products': products})


def PaymentPage(request):
    title = 'Корзина'
    basket = Basket.objects.all()

    if request.method == 'POST':
        if 'product_delete' in request.POST:

            # Если нажата кнопка удаления товара

            product = Basket.objects.get(pk=request.POST['id'])  # Получение продукта из корзины по id
            product.delete()  # Удаление продукта из корзины

            logger.error('Продукт удален из корзины')

        if 'order' in request.POST:

            # Если нажата кнопка оформления заказа

            order = Order()  # Объявляем экземпляр заказа

            # Получение необходимых данных из формы
            order.name = request.POST['name']
            order.phone = request.POST['phone']
            order.delivery = request.POST['delivery']
            order.total_sum = int(request.POST['total_sum'].split()[0])

            order.save()  # Сохранение заказа в базе данных
            products = Basket.objects.all()  # Выгрузка всей корзины

            for p in products:
                order.basket.add(p)  # Добавление продуктов в заказ
            logger.error('Заказ оформлен')

    logger.error('Загрузка страницы корзины и оплаты')
    return render(request, 'main/PaymentPage.html', {'title': title, 'basket': basket})


def add_to_basket(request):
    if request.method == 'POST':
        basket = Basket.objects.all()  # Выгрузка всей корзины
        product = Product.objects.get(pk=request.POST['product_id'])  # Получение продукта по заданному значению id
        # Проверка на существование продукта в корзине
        product_exists = basket.filter(product_id=request.POST['product_id']).exists()
        logger.error('Существование продукта в корзине: ' + str(product_exists))

        if product_exists:

            # Если продукт существует в корзине, то увеличим его количество на 1

            upd_product = basket.get(product_id=product)  # Получение продукта для обновления из корзины
            Basket.objects.filter(product_id=product).update(count=upd_product.count + 1)  # Обновление значения количества
            upd_product.refresh_from_db()  # Обновление продукта в базе данных
            logger.error('Продукт обновлен в корзине')
        else:

            # Если продукта в корзине нет, то просто добавляем его в корзину

            basket_ = Basket()  # Объявляем экземпляр корзины
            basket_.product_id = product  # Присвоение значение продукта в корзине
            basket_.save()  # Сохранение нового продукта в корзине
            logger.error('Продукт в корзину добавлен')
