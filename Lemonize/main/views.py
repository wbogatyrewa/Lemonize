from django.shortcuts import render
from .models import Product, Basket


def MainPage(request):
    return render(request, 'main/MainPage.html')


def ProductPagePastries(request):
    title = 'Пирожные'
    products = Product.objects.filter(type=title)
    if request.method == 'POST':
        basket = Basket()
        basket.product_id = Product.objects.get(pk=request.POST['product_id'])
        basket.save()
    return render(request, 'main/ProductPage.html', {'title': title, 'products': products})


def ProductPageCakes(request):
    title = 'Торты'
    products = Product.objects.filter(type=title)
    if request.method == 'POST':
        basket = Basket()
        basket.product_id = Product.objects.get(pk=request.POST['product_id'])
        basket.save()
    return render(request, 'main/ProductPage.html', {'title': title, 'products': products})


def ProductPageMacaroons(request):
    title = 'Макаруны'
    products = Product.objects.filter(type=title)
    if request.method == 'POST':
        basket = Basket()
        basket.product_id = Product.objects.get(pk=request.POST['product_id'])
        basket.save()
    return render(request, 'main/ProductPage.html', {'title': title, 'products': products})


def PaymentPage(request):
    title = 'Корзина'
    basket = Basket.objects.all()
    return render(request, 'main/PaymentPage.html', {'title': title, 'basket': basket})