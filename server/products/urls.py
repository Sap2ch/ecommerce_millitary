from django.urls import path
from .views import CreateProductView, ListProductView, MyProductsView, ShowProductsView

urlpatterns = [
    path('create-products/', CreateProductView.as_view(), name='create-products'),
    path('products/', ListProductView.as_view(), name='products'),
    path('my-products/', MyProductsView.as_view(), name='my-products'),
    path('products/<slug:slug>/', ShowProductsView.as_view(), name='show-products'),
]