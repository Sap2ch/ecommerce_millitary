from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.text import slugify

from .forms import AddProductForm
from .models import Products

class CreateProductView(LoginRequiredMixin, generic.CreateView):
    form_class = AddProductForm
    template_name = 'add-product.html'
    success_url = reverse_lazy('home')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.user = self.request.user  # Присваиваем текущего пользователя
        
        return super().form_valid(form)
    
class ListProductView(LoginRequiredMixin, generic.ListView):
    form_class = AddProductForm
    model = Products
    template_name = 'products.html'
    context_object_name = 'products'

class MyProductsView(LoginRequiredMixin, generic.ListView):
    template_name = 'my-products.html'
    model = Products  
    context_object_name = 'products'
    login_url = 'login'
    
    def get_queryset(self) -> QuerySet[Any]:
        return Products.objects.filter(user=self.request.user)
    
class ShowProductsView(generic.DetailView):
    template_name = 'show-products.html'
    model = Products
    context_object_name = 'product'