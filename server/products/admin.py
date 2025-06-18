from django.contrib import admin
from .models import Products

class ProductsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'description', 'slug', 'type_gun', 'caliber', 'state', 'phone', 'payload_methods', 'price', 'image', 'user')
    list_display_links = ('pk', 'user')

    class Meta:
        verbose_name = 'Products'
        verbose_name_plural = 'Products'

admin.site.register(Products, ProductsAdmin)
