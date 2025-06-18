from typing import Any
from django.forms import ModelForm
from .models import Products

class AddProductForm(ModelForm):
    class Meta:
        model = Products
        fields = ('title', 'description', 'type_gun', 'caliber', 'state', 'phone', 'payload_methods', 'price', 'image')

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Получаем пользователя из аргументов
        super().__init__(*args, **kwargs)
        if user:
            self.instance.user = user  # Устанавливаем пользователя для текущего экземпляра