from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from category.models import Category
from django.views import View


class IndexView(View):
    def get(self, request):
        return render(request, 'index.html', context={'request': request})

class AmmoView(View):
    def get(self, request):
        return render(request, 'ammo.html')
    
class AboutView(View):
    def get(self, request):
        return render(request, 'about.html')
    


# def index(request):
#     return render(request, 'index.html', context={'request': request})

# def ammo(request):
#     return render(request, 'ammo.html')

# def about(request):
#     return render(request, 'about.html')


# class IndexView(ListView):
#     template_name = 'index.html'
#     content_type = 'request'
#     model = Category
