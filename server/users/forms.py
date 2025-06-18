from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import FFLVerify

class FFLForm(forms.ModelForm):
    # ffl_verifed = forms.ImageField(label='FFL license: ')
    class Meta:
        model = FFLVerify
        fields = ('image',)