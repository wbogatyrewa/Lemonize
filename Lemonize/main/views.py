from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def MainPage(request):
    return render(request, 'main/MainPage.html')


def ProductPage(request):
    return render(request, 'main/ProductPage.html')


def PaymentPage(request):
    return render(request, 'main/PaymentPage.html')