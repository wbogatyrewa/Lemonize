from django.urls import path
from . import views

urlpatterns = [
    path('', views.MainPage, name='home'),
    path('ProductPage', views.ProductPage, name='products'),
    path('PaymentPage', views.PaymentPage, name='payment')
]