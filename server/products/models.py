from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from datetime import datetime

# class Products(models.Model):
#     title = models.CharField(max_length=255, verbose_name='Заголовок')
#     description = models.TextField(verbose_name='Опис')
#     type_gun = models.CharField(max_length=50, verbose_name='Тип зброї')
#     caliber = models.FloatField(verbose_name='Калібр')
#     state = models.CharField(max_length=50, verbose_name='Штат проживання')
#     country = models.CharField(max_length=50, verbose_name='Держава проживання')
#     phone = models.CharField(max_length=20, verbose_name='Номер телефону')
#     payload_methods = models.CharField(max_length=100, verbose_name='Вибір оплати')
#     price = models.FloatField(verbose_name='Ціна')
#     user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Продавець')

class Products(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Опис')
    slug = models.SlugField(max_length=255, unique=True, null=True, verbose_name='URL')
    type_gun = models.CharField(max_length=50, verbose_name='Тип зброї')
    caliber = models.FloatField(verbose_name='Калібр')
    state = models.CharField(max_length=50, verbose_name='Штат проживання')
    phone = models.CharField(max_length=20, verbose_name='Номер телефону')
    payload_methods = models.CharField(max_length=100, verbose_name='Вибір оплати')
    price = models.FloatField(verbose_name='Ціна')
    image = models.ImageField(upload_to='products/%Y/%m/%d/', null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Продавець')

    def __str__(self) -> str:
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.generate_unique_slug(self.title)
        super().save(*args, **kwargs)

    def generate_unique_slug(self, title):
        slug = slugify(title)
        while Products.objects.filter(slug=slug).exists():
            slug = f'{slug}-{Products.objects.filter(slug__startswith=slug).count() + 1}'
        return slug