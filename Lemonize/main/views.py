from django.shortcuts import render
from .models import Product


def MainPage(request):
    return render(request, 'main/MainPage.html')


def ProductPagePastries(request):
    title = 'Пирожные'
    products = Product.objects.filter(type=title)
    return render(request, 'main/ProductPage.html', {'title': title, 'products': products})


def ProductPageCakes(request):
    title = 'Торты'
    products = Product.objects.filter(type=title)
    return render(request, 'main/ProductPage.html', {'title': title, 'products': products})


def ProductPageMacaroons(request):
    title = 'Макаруны'
    products = Product.objects.filter(type=title)
    return render(request, 'main/ProductPage.html', {'title': title, 'products': products})

def PaymentPage(request):
    title = 'Корзина'
    products = []
    return render(request, 'main/PaymentPage.html', {'title': title, 'products': products})