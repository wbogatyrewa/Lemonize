from django.shortcuts import render
from .models import Product, Basket, Order
import logging
logger = logging.getLogger(__name__)

def MainPage(request):
    return render(request, 'main/MainPage.html')


def ProductPagePastries(request):
    title = 'Пирожные'
    products = Product.objects.filter(type=title)
    load(request)
    return render(request, 'main/ProductPage.html', {'title': title, 'products': products})


def ProductPageCakes(request):
    title = 'Торты'
    products = Product.objects.filter(type=title)
    load(request)
    return render(request, 'main/ProductPage.html', {'title': title, 'products': products})


def ProductPageMacaroons(request):
    title = 'Макаруны'
    products = Product.objects.filter(type=title)
    load(request)
    return render(request, 'main/ProductPage.html', {'title': title, 'products': products})


def PaymentPage(request):
    title = 'Корзина'
    basket = Basket.objects.all()
    if request.method == 'POST':
        if 'product_delete' in request.POST:
            product = Basket.objects.get(pk=request.POST['id'])  # получение продукта по id
            product.delete()  # удаление продукта из корзины

        if 'order' in request.POST:
            order = Order()

            order.name = request.POST['name']
            order.phone = request.POST['phone']
            order.delivery = request.POST['delivery']
            order.total_sum = int(request.POST['total_sum'].split()[0])

            order.save()
            products = Basket.objects.all()
            for p in products:
                order.basket.add(p)

    return render(request, 'main/PaymentPage.html', {'title': title, 'basket': basket})


def load(request):
    if request.method == 'POST':
        basket = Basket.objects.all()
        product = Product.objects.get(pk=request.POST['product_id'])
        product_exists = basket.filter(product_id=request.POST['product_id']).exists()
        logger.error(product_exists)
        if product_exists:
            upd_product = basket.get(product_id=product)
            Basket.objects.filter(product_id=product).update(count=upd_product.count + 1)
            upd_product.refresh_from_db()
            logger.error(basket.get(product_id=product).count)
        else:
            basket_ = Basket()
            product = Product.objects.get(pk=request.POST['product_id'])
            basket_.product_id = product
            basket_.save()