from typing import Any, Dict
from django.db import models
from django.forms.models import BaseModelForm
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, FormView
from django.http import Http404, HttpRequest, HttpResponse, HttpResponseRedirect
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Profile, FFLVerify
from .forms import FFLForm

def custom_page_not_found(request, exception):
    return render(request, '404.html', status=404)

def logout_user(request):
    logout(request)
    
    return HttpResponseRedirect(reverse('home'))

class ProfileView(DetailView):
    model = Profile
    template_name = 'profile.html'

    # def get_object(self):
    #     try:
    #         obj = Profile.objects.get(slug=self.kwargs['slug'])
    #     except Profile.DoesNotExist:
    #         raise render(self.request, './profile.html', context={'request': self.request, 'slug': self.kwargs['slug']})
    #     return obj
    
    def get(self, request, slug):
        try:
            obj = Profile.objects.get(slug=self.kwargs['slug'].lower())
        except Profile.DoesNotExist:
            raise render(self.request, './profile.html', context={'request': self.request, 'slug': self.kwargs['slug'].lower()})
        
        return render(request, './profile.html', context={'request': request, 'slug': self.kwargs['slug'].lower(), 'profile': obj})
    

class UsersView(ListView):
    model = Profile
    template_name = 'users.html'
    context_object_name = 'profiles'
    # paginate_by = 


class FFLView(LoginRequiredMixin, CreateView):
    model = FFLVerify   # зареєстрована моделька з якою ми працюємо
    form_class = FFLForm    # форма з якою ми працюємо
    template_name = 'ffl_page.html'     # шаблон з яким ми працюємо
    success_url = reverse_lazy('home')
    login_url = 'login'

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        """
            До поля user (FK) прив'язуємо поточного користувача
        """
        form.instance.user = self.request.user

        return super().form_valid(form)
    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)    # звертаємось до батьківського класу і зберігаємо у змінну всі дані

        if len(FFLVerify.objects.filter(user=self.request.user)) != 0:
            context['user_ffl'] = FFLVerify.objects.get(user=self.request.user)  # змінено
        # context['image'] = FFLVerify.objects.filter(user=self.request.user)[0].image.url

        return context



handler404 = custom_page_not_found