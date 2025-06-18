from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('ammo/', AmmoView.as_view(), name='ammo'),
    path('about/', AboutView.as_view(), name='about'),
]
