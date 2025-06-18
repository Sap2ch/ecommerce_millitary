from typing import Any
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from users.models import Profile
from django import forms


class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField(required=True, max_length=64)
    first_name = forms.CharField(required=True, max_length=30)
    last_name = forms.CharField(required=True, max_length=30)
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(required=True, max_length=15)
    state = forms.ChoiceField(required=True, choices=Profile.STATES)
    status = forms.ChoiceField(required=True, choices=[('Buyer', 'Buyer'), ('Seller', 'Seller')])
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'phone_number', 'state', 'status']

    def clean_username(self):
        username = self.cleaned_data.get('username')
        
        if len(User.objects.filter(username=username)) > 0:
            raise ValidationError("User is active")
        
        if len(User.objects.filter(username=username.lower())) > 0:
            raise ValidationError("User is active")
        
        # if User.objects.filter(username=username).exists():
        #     raise ValidationError("Этот логин уже занят.")
        
        return username.lower() # зберігаємо юзернейм в нижньому регістрі

    def clean_password_confirm(self):
        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data.get('password_confirm')

        if password != password_confirm:
            raise ValidationError("Пароли не совпадают")
        
        return password_confirm
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Этот email уже занят.")
        
        return email


    def save(self, commit: bool = ...) -> Any:
        user = super().save(commit=False)

        if commit:
            user.save()
            
        data = self.cleaned_data
        
        profile, created = Profile.objects.get_or_create(
            user=user,
            slug=data['username'].lower(),
            phone_number=data['phone_number'],
            state=data['state'],
            status=data['status']
        )
        
        if commit:
            profile.save()
        
        return user


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=100)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    
