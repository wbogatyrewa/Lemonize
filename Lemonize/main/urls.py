from django.urls import path
from . import views

urlpatterns = [
    path('', views.MainPage, name='home'),
    path('ProductPagePastries', views.ProductPagePastries, name='pastries'),
    path('ProductPageCakes', views.ProductPageCakes, name='cakes'),
    path('ProductPageMacaroons', views.ProductPageMacaroons, name='macaroons'),
    path('PaymentPage', views.PaymentPage, name='payment')
]