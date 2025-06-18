from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=50, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, verbose_name='URL')