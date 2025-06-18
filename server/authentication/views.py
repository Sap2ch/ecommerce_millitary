from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegistrationForm, LoginForm
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView

from .forms import LoginForm, UserRegistrationForm


class RegisterView(CreateView):
    form_class = UserRegistrationForm
    template_name = 'register.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        valid = super(RegisterView, self).form_valid(form)

        if form.is_valid():
            user = form.save()
            user.backend = 'django.contrib.auth.backends.ModelBackend'  # установка дефолтної реєстрації
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(self.request, user)  # автоматически авторизуем пользователя после регистрации

        return valid
    
    
class LoginUser(LoginView):
    form_class = LoginForm
    template_name = 'login.html'
    success_url = reverse_lazy('/')


    def form_valid(self, form):
        """
            РЕАЛІЗОВАНА СИСТЕМА ВХОДУ БЕЗ ВРАХУВАННЯ РЕГІСТРУ ЮЗЕРНЕЙМУ,
            ЯКЩО НЕ ПІДІЙДЕ ЦЯ СИСТЕМА, ТО МОЖНА ЇЇ ВИДАЛИТИ
        """
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')

        user = authenticate(self.request, username=username, password=password)

        if user is not None:
            login(self.request, user)
            return redirect('home') 

        form.add_error(None, 'Неверный логин или пароль.')
        return self.form_invalid(form)


# def register(request):
#     if request.method == 'POST':
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             user.set_password(user.password)
#             user.save()
#             login(request, user)  # автоматически авторизуем пользователя после регистрации
#             return redirect('home')  # редирект на домашнюю страницу
#     else:
#         form = UserRegistrationForm()

#     return render(request, './register.html', {'form': form})


# def login_auth(request):
#     if request.method == "POST":
#         form = LoginForm(request, data=request.POST)
#         print(form.get_user())
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             return redirect('home')  # Replace 'home' with the name of your homepage URL
#     else:
#         form = LoginForm()

#     return render(request, './login.html', {'form': form})